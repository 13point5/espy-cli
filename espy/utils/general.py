import os
import click
import sys
from terminaltables import AsciiTable


def is_dir(dir_path):
	return os.path.isdir(dir_path)


def is_file(filepath):
	return os.path.exists(filepath)


def write_file(filepath, data):
	file = open(filepath, 'w')
	file.write(data)
	file.close()


def get_json(jbon, key, value):
	for obj in jbon:
		if obj[key] == value:
			return [obj]
	return None


def is_json_dup(jbon, key, value):
	if get_json(jbon, key, value) is not None:
		return True
	return False


def disp_json(jbon, keys):
	data = [keys]
	for obj in jbon:
		data.append( [obj[key] for key in keys] )
	table = AsciiTable(data)
	click.echo(table.table)


def disp_err(msg, exit=None):
	click.echo(msg, err=True)
	if exit:
		sys.exit(1)
