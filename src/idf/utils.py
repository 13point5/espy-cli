import os
import click
import sys
from src.utils.general import *
from src.utils.config import *
from src.utils.constants import *


def new_idf(name, filepath):
	if not is_dir(filepath):
		disp_err("The specified path does not exist.", exit=True)

	os.chdir(filepath)
	filepath = os.getcwd()

	config = config_read()
	config_idf = config[SECTION_IDF]
	if not is_json_dup(config_idf, "name", name):
		if not is_json_dup(config_idf, "filepath", filepath):
			config_idf.append({
				"name": name,
				"filepath": filepath
			})
			config_write(config)
			return "\nSuccessfully added {} to config".format(name)
		else:
			disp_err("The specified path already exists in the config", exit=True)
	else:
		disp_err("The specified name for IDF already exists in the config", exit=True)


def mod_idf(name):
	config = config_read()
	config_idf = config[SECTION_IDF]

	obj_idx = get_json(config_idf, "name", name, idx=True)
	if obj_idx is None:
		disp_err("Could not find required IDF", exit=True)

	disp_json([config_idf[obj_idx]], ["name", "filepath"])

	new_name = None
	if click.confirm("\nChange the name?"):
		new_name = click.prompt("Enter the new name for the IDF")
		if is_json_dup(config_idf, "name", new_name):
			disp_err("{} already exists.".format(new_name), exit=True)
		config_idf[obj_idx]["name"] = new_name

	new_filepath = None
	if click.confirm("\nChange the path of the IDF?"):
		new_filepath = click.prompt("Enter the new path for the IDF").rstrip("/")
		if is_json_dup(config_idf, "filepath", new_filepath):
			disp_err("Specified IDF path already exists.".format(new_name), exit=True)
		config_idf[obj_idx]["filepath"] = new_filepath

	click.confirm("\nNote: If this IDF has been used in an app, modify them accordingly.\nContinue to modify IDF?", abort=True)

	config[SECTION_IDF] = config_idf
	config_write(config)
	return "\nSuccessfully modified the IDF"


def remove_idf(name):
	config = config_read()
	config_idf = config[SECTION_IDF]
	if is_empty(config_idf):
		return "\nThere is nothing to remove."

	if name:
		obj_idx = get_json(config_idf, "name", name, idx=True)

		if obj_idx is None:
			disp_err("Could not find required IDF", exit=True)
		else:
			click.confirm("\nNote: If this IDF has been used in an app, modify them accordingly.\nContinue to delete IDF?", abort=True)
			del config_idf[obj_idx]

	else:
		click.confirm("\nDelete all IDFs?", abort=True)
		config_idf = []

	config[SECTION_IDF] = config_idf
	config_write(config)
	return "\nSuccessfully deleted required IDF(s)"
