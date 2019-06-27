import os
import click
from src.utils.general import *
from src.utils.config import *
from src.idf.utils import *


def new_app(dir_name, dir_path, idfname):
	cur_path = os.getcwd()
	if not dir_path:
		dir_path = cur_path

	if not is_dir(dir_path):
		click.echo("\nThe specified directory path does not exist.")
		click.confirm("Countinue to make the directory?", abort=True)
		os.makedirs(dir_path)

	os.chdir(dir_path)
	dir_path = os.getcwd()

	proj_path = os.path.join(dir_path, dir_name)
	if is_dir(proj_path):
		disp_err("\nDirectory with given project name already exists", exit=True)


	idf_data = get_data(SECTION_IDF, "name", idfname)
	idf_path = idf_data[0]["filepath"]

	proj_main_path = os.path.join(proj_path, "main")
	os.makedirs(proj_main_path)

	"""
	root dir files
	"""
	makefile_data = "PROJECT_NAME := {}\n\nIDF_PATH = {}\n\ninclude $(IDF_PATH)/make/project.mk".format(dir_name, idf_path)
	write_file(os.path.join(proj_path, "Makefile"), makefile_data)

	root_cmake_data = "cmake_minimum_required(VERSION 3.5)\n\ninclude({}/tools/cmake/project.cmake)\nproject({})".format(idf_path, dir_name)
	write_file(os.path.join(proj_path, "CMakelists.txt"), root_cmake_data)

	"""
	main dir files
	"""
	main_cmake_data = 'set(COMPONENT_SRCS "main.c")\nset(COMPONENT_ADD_INCLUDEDIRS "")\n\nregister_component()'
	write_file(os.path.join(proj_main_path, "CMakelists.txt"), main_cmake_data)

	main_compmk_data = '#\n# "main" pseudo-component makefile.'
	write_file(os.path.join(proj_main_path, "component.mk"), main_compmk_data)

	main_app_data = '#include <stdio.h>\n\n\nvoid app_main() {\n\tprintf("Hello world!\\n");\n}'
	write_file(os.path.join(proj_main_path, "main.c"), main_app_data)

	"""
	writing to config
	"""
	config = config_read()
	config_app = config[SECTION_APP]
	if not is_json_dup(config_app, "name", dir_name):
		if not is_json_dup(config_app, "filepath", proj_path):
			config_app.append({
				"name": dir_name,
				"filepath": proj_path,
				"idf": idfname,
				"idfpath": idf_path
			})
			config_write(config)
		else:
			disp_err("The specified filepath already exists in the config", exit=True)
	else:
		disp_err("The specified App name already exists in the config", exit=True)

	return "\nProject created!"


def modify_app(app_idx, opts, opt_msgs):

	config = config_read()
	config_app = config[SECTION_APP]
	app_data = config_app[app_idx]
	proj_path = app_data["filepath"]

	new_app_data = None
	new_idf_data = None

	for o in range(len(opts)):
		if opts[o] == True:
			if opt_msgs[o] == "Name":
				new_app_data = change_name(config_app, app_data)
				if new_app_data:
					config_app[app_idx]["name"] = new_app_data[0]
					config_app[app_idx]["filepath"] = new_app_data[1]

			if opt_msgs[o] == "IDF":
				new_idf_data = change_idf(app_data)
				if new_idf_data:
					config_app[app_idx]["idf"] = new_idf_data[0]
					config_app[app_idx]["idfpath"] = new_idf_data[1]


	if new_app_data or new_idf_data:
		config[SECTION_APP] = config_app
		config_write(config)
		return "\nSuccessfully modified app details!"

	return "\nNothing changed."



def change_name(config_app, data):

	new_name = click.prompt("\nEnter new name")
	if is_json_dup(config_app, "name", new_name):
		disp_err("{} already exists in config".format(new_name), exit=True)

	proj_path = data["filepath"]

	os.chdir(proj_path)
	os.chdir("..")

	new_filepath = (os.path.join(os.getcwd(), new_name))
	if is_dir(new_filepath):
		disp_err("\nDirectory with new app name exists", exit=True)

	makefile_path = os.path.join(proj_path, "Makefile")
	if not is_file(makefile_path):
		disp_err("Could not find Makefile", exit=True)

	cmake_path = os.path.join(proj_path, "CMakelists.txt")
	if not is_file(cmake_path):
		disp_err("Could not find CMakelists.txt", exit=True)

	makefile_data = read_file(makefile_path)
	for i in range(len(makefile_data)):
		if 'PROJECT_NAME' == makefile_data[i][:12]:
			makefile_data[i] = "PROJECT_NAME := {}\n".format(new_name)
			break
	makefile_data = "".join(makefile_data)

	cmake_data = read_file(cmake_path)
	for i in range(len(cmake_data)):
		if cmake_data[i].strip("\n") == "project({})".format(data["name"]):
			cmake_data[i] = "project({})\n".format(new_name)
			break
	cmake_data = "".join(cmake_data)


	if click.confirm("Change the name of the project?"):
		write_file(makefile_path, makefile_data)
		write_file(cmake_path, cmake_data)
		os.rename(proj_path, new_filepath)
		click.echo("\nName changed.")
		return [new_name, new_filepath]

	return None


def change_idf(data):

	new_idf_name = click.prompt("\nEnter new IDF's name")
	config = config_read()
	config_idf = config[SECTION_IDF]

	idf_idx = get_json(config_idf, "name", new_idf_name, True)
	if idf_idx is None:
		disp_err("\nCould not find required IDF", exit=True)

	new_idf_path = config_idf[idf_idx]["filepath"]
	old_idf_path = data["idfpath"]

	proj_path = data["filepath"]

	makefile_path = os.path.join(proj_path, "Makefile")
	if not is_file(makefile_path):
		disp_err("Could not find Makefile", exit=True)

	cmake_path = os.path.join(proj_path, "CMakelists.txt")
	if not is_file(cmake_path):
		disp_err("Could not find CMakelists.txt", exit=True)

	makefile_data = read_file(makefile_path)
	for i in range(len(makefile_data)):
		if makefile_data[i].strip("\n") == "IDF_PATH = {}".format(old_idf_path):
			makefile_data[i] = "\nIDF_PATH = {}\n".format(new_idf_path)
			break
	makefile_data = "".join(makefile_data)

	cmake_data = read_file(cmake_path)
	for i in range(len(cmake_data)):
		if cmake_data[i].strip("\n") == "include({}/tools/cmake/project.cmake)".format(old_idf_path):
			cmake_data[i] = "\ninclude({}/tools/cmake/project.cmake)\n".format(new_idf_path)
			break
	cmake_data = "".join(cmake_data)

	if click.confirm("Change the IDF of the project?"):
		write_file(makefile_path, makefile_data)
		write_file(cmake_path, cmake_data)
		click.echo("\nIDF changed.")
		return [new_idf_name, new_idf_path]

	return None


def remove_app(name):
	config = config_read()
	config_app = config[SECTION_APP]
	if name:
		obj_idx = get_json(config_app, "name", name, idx=True)

		if obj_idx is None:
			disp_err("Could not find required App", exit=True)
		else:
			click.confirm("Delete app: {}?".format(name), abort=True)
			del config_app[obj_idx]
	else:
		click.confirm("Delete all Apps?", abort=True)
		config_app = []

	config[SECTION_APP] = config_app
	config_write(config)
	return "\nSuccessfully deleted required App(s)"
