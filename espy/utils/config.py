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
					"Please add atleast 1 IDF path in order to create apps.".format(CONFIG_FILE))
		return False

	return True


def config_check():
	"""
	Check if the config file is not corrupted
	"""
	config = config_read()

	if not config[SECTION_IDF]:
		click.echo("Please add atleast 1 IDF path in order to create apps.")
		return False

	return True


def config_init():
	"""
	Initialise configurations
	"""
	if config_exists():
		if not config_check():
			sys.exit(1)
		pass
	else:
		sys.exit(1)
