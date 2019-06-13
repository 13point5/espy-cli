"""
Commands to manage IDF paths
"""

import click
from espy.idf import utils

@click.command()
@click.option('-n', '--name', required=True, type=click.STRING, help='Name of the IDF. Must be unique')
@click.option('-f', '--filepath', required=True, type=click.STRING, help='Path to the IDF')
def create_idf(name, filepath):
	"""
	Add a new IDF with the given name and filepath
	"""
	click.echo(utils.new_idf(name, filepath))
