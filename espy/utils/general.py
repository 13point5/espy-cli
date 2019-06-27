import os
import click
import sys
from terminaltables import AsciiTable


def is_dir(dir_path):
	return os.path.isdir(dir_path)


def is_file(filepath):
	return os.path.exists(filepath)


def read_file(filepath):
	file = open(filepath, 'r')
	data = file.readlines()
	file.close()
	return data


def write_file(filepath, data):
	file = open(filepath, 'w')
	file.write(data)
	file.close()


def get_json(jbon, key, value, idx=False):
	for i in range(len(jbon)):
		if jbon[i][key] == value:
			if idx:
				return i
			return [jbon[i]]
	return None


def is_json_dup(jbon, key, value):
	if get_json(jbon, key, value) is not None:
		return True
	return False


def is_empty(jbon):
	return len(jbon) == 0


def disp_json(jbon, keys):
	data = [keys]
	for obj in jbon:
		data.append( [obj[key] for key in keys] )
	table = AsciiTable(data)
	click.echo()
	click.echo(table.table)


def disp_err(msg, exit=None):
	click.echo("\n" + msg, err=True)
	if exit:
		sys.exit(1)
