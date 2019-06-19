import os
import click
from espy.utils.general import *
from espy.idf.utils import *


def new_app(dir_name, dir_path, idfname):
	cur_path = os.getcwd()
	if not dir_path:
		dir_path = cur_path

	#dir_path = dir_path.rstrip('/')

	if not is_dir(dir_path):
		click.echo("The specified directory path does not exist.")
		click.confirm("Countinue to make the directory?", abort=True)
		os.makedirs(dir_path)

	proj_path = os.path.join(dir_path, dir_name)
	if is_dir(proj_path):
		disp_err("Directory with given project name already exists", exit=True)

	idf_path = get_idf(idfname)[0]["filepath"]

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
		disp_err("The specified name for App already exists in the config", exit=True)

	return "Project created!"


def modify_app(data, opts, opt_msgs):

	click.echo(data)

	for o in range(len(opts)):
		if opts[o] == True:
			if opt_msgs[o] == "Name":
				pass
