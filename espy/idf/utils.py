import os
import click
import sys
from espy.utils.general import *
from espy.utils.config import *
from espy.utils.constants import *


def new_idf(name, filepath):
	if not is_dir(filepath):
		disp_err("The specified path does not exist.", exit=True)

	config = config_read()
	config_idf = config[SECTION_IDF]
	if not is_json_dup(config_idf, "name", name):
		if not is_json_dup(config_idf, "filepath", filepath):
			config_idf.append({
				"name": name,
				"filepath": filepath
			})
			config_write(config)
			return "Successfully added {} to config".format(name)
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

	new_name = click.prompt("Enter the new name for the IDF")
	new_filepath = None

	if click.confirm("\nChange the path of the IDF?"):
		new_filepath = click.prompt("Enter the new path for the IDF").rstrip("/")

	click.confirm("\nNote: If this IDF has been used in an app, modify them if needed.\nContinue to modify IDF?", abort=True)

	config_idf[obj_idx]["name"] = new_name
	if new_filepath is not None:
		config_idf[obj_idx]["filepath"] = new_filepath

	config[SECTION_IDF] = config_idf
	config_write(config)
	return "Successfully modified the IDF"


def remove_idf(name):
	config = config_read()
	config_idf = config[SECTION_IDF]
	if name:
		k=-1
		for i in range(len(config_idf)):
			if config_idf[i]["name"] == name:
				k=i
				break
		if k==-1:
			disp_err("Could not find the required IDF", exit=True)
		else:
			click.confirm("Delete IDF: {}".format(name), abort=True)
			del config_idf[k]
	else:
		click.confirm("Delete all IDFs?", abort=True)
		config_idf = []

	config[SECTION_IDF] = config_idf
	config_write(config)
	return "Successfully deleted required IDF(s)"
