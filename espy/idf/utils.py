import os
import click
import sys
from espy.utils.general import *
from espy.utils.config import *
from espy.utils.constants import *


def new_idf(name, filepath):
	if not is_dir(filepath):
		disp_err("The specified path does not exist.", exit=True)

	filepath = filepath.rstrip("/")

	config = config_read()
	config_idf = config[SECTION_IDF]
	if not is_json_dup(config_idf, "name", name):
		if not is_json_dup(config_idf, "filepath", filepath):
			config_idf.append({
				"name": name,
				"filepath": filepath
			})
			config_write(config)
			return "Succesfully added {} to config".format(name)
		else:
			disp_err("The specified path already exists in the config", exit=True)
	else:
		disp_err("The specified name for IDF already exists in the config", exit=True)


def get_idf(name=None):
	config = config_read()
	config_idf = config[SECTION_IDF]

	data = config_idf
	if name:
		data = get_json(config_idf, "name", name)
		if data is None:
			disp_err("Could not find the required IDF", exit=True)

	return data


def remove_idf(name=None):
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
			del config_idf[k]
	else:
		click.confirm("Delete all IDFs?", abort=True)
		config_idf = []

	config[SECTION_IDF] = config_idf
	config_write(config)
	return "Succesfully deleted required IDF(s)"
