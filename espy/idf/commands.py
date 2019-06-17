"""
Commands to manage IDF paths
"""

import click
from . import utils
from espy.utils.general import disp_json

@click.command()
@click.option('-n', '--name', required=True, type=click.STRING, help='Name of the IDF. Must be unique')
@click.option('-f', '--filepath', required=True, type=click.STRING, help='Path to the IDF')
def create_idf(name, filepath):
	"""
	Add a new IDF with the given name and filepath
	"""
	click.echo(utils.new_idf(name, filepath))


@click.command()
@click.option('-n', '--name', type=click.STRING, help='Name of the IDF. Must be unique')
def find_idf(name):
	"""
	Find all or specified IDF(s)
	"""
	data = utils.get_idf(name)
	disp_json(data, ["name", "filepath"])


@click.command()
@click.option('-n', '--name', type=click.STRING, help='Name of the IDF. Must be unique')
def delete_idf(name):
	"""
	Delete all or specified IDF(s)
	"""
	click.echo(utils.remove_idf(name))
