import os
import click
import espy
import sys
import json
from appdirs import user_config_dir

SECTION_IDF = 'IDFs'
SECTION_APP = 'Apps'

CONFIG_DIR = user_config_dir("esp-cli")
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')


def is_dir(dir_path):
	return os.path.isdir(dir_path)


def is_file(filepath):
	return os.path.exists(filepath)


def is_json_dup(jbon, key, value):
	for obj in jbon:
		if obj[key] == value:
			return True
	return False


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
