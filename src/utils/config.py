import json
import os
import click
from .constants import *
from .general import *

def config_read():
	"""
	Read from config file
	"""
	with open(CONFIG_FILE, 'r') as cnf_file:
		return json.load(cnf_file)


def config_disp():
	"""
	Display config
	"""
	click.echo("\nConfig location: {}".format(CONFIG_FILE))

	idf_data = get_data(SECTION_IDF)
	click.echo("\nIDFs")
	disp_json(idf_data, ["name", "filepath"])

	app_data = get_data(SECTION_APP)
	click.echo("\nApps")
	disp_json(app_data, ["name", "filepath", "idf", "idfpath"])


def config_write(new_config):
	"""
	Write to config file
	"""
	with open(CONFIG_FILE, 'w') as cnf_file:
		json.dump(new_config, cnf_file)


def config_exists():
	"""
	Create a config file if it doesn't exist.
	"""
	if not is_file(CONFIG_FILE):
		if not is_dir(CONFIG_DIR):
			os.makedirs(CONFIG_DIR)

		empty_config = {SECTION_IDF: [], SECTION_APP: []}
		with open(CONFIG_FILE, 'w') as cnf_file:
			json.dump(empty_config, cnf_file)

		click.echo("\nAn empty configuration file has been created.\n"
					"Please add atleast 1 IDF path in order to create apps.")
		return False

	if config_check(SECTION_APP) and config_check(SECTION_IDF):
		return True

	disp_err("Config file is corrupted. Kindly correct it or delete it to create an empty configuration.", exit=True)


def config_check(section):
	"""
	Check if the config file is not corrupted
	"""
	config = config_read()

	try:
		data = config[section]
		return True
	except Exception as e:
		return False


def get_data(section, key=None, value=None, idx=False):
	"""
	Get data from config
	"""
	config = config_read()
	config_section = config[section]

	data = config_section
	if value and key:
		data = get_json(config_section, key, value, idx)
		if data is None:
			disp_err("Could not find the required {}".format(section), exit=True)

	return data
