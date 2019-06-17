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

		click.echo("A blank configuration file has been created at {}\n"
					"Please add atleast 1 IDF path in order to create apps.\n".format(CONFIG_FILE))
		return False

	return True


def config_check(section):
	"""
	Check if the config file is not corrupted
	"""
	config = config_read()

	if not config[section]:
		disp_err("{} config is empty".format(section))
		return False

	return True


def get_data(section, key=None, value=None):
	config = config_read()
	config_section = config[section]

	data = config_section
	if value and key:
		data = get_json(config_section, key, value)
		if data is None:
			disp_err("Could not find the required {}".format(section), exit=True)

	return data
