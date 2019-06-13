import os
import click
import sys
from espy.gen_utils import *


def new_idf(name, filepath):
	if not is_dir(filepath):
		click.echo("The specified path does not exist.", err=True)
		sys.exit(1)

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
			click.echo("The specified path already exists in the config", err=True)
			sys.exit(1)
	else:
		click.echo("The specified name for IDF already exists in the config", err=True)
		sys.exit(1)
