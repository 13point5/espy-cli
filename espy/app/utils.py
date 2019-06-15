import os
import click
from espy.utils.general import *
from espy.idf.utils import *


def new_app(dir_name, dir_path, idfname):
	cur_path = os.getcwd()
	if not dir_path:
		dir_path = cur_path

	if not is_dir(dir_path):
		click.echo("The specified directory path does not exist.")
		click.confirm("Countinue to make the directory?", abort=True)
		os.makedirs(dir_path)

	proj_path = os.path.join(dir_path, dir_name)
	if is_dir(proj_path):
		disp_err("Directory with given project name already exists", exit=True)


	proj_main_path = os.path.join(proj_path, "main")
	os.makedirs(proj_main_path)

	idf_path = get_idf(idfname)[0]["filepath"]

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

	return "Project created!"
