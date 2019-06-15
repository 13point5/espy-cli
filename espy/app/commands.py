"""
Commands to manage an app
"""

import click
from espy.app import utils
from espy.utils import config

@click.command()
@click.option('-n', '--name', type=click.STRING, required=True, help='Name of the app')
@click.option('-f', '--filepath', type=click.STRING, help='Path to directory where app will be created')
@click.option('-idf', '--idfname', type=click.STRING, required=True, help='Name of IDF saved in config')
def create_app(name, filepath, idfname):
	"""
	Create a new app with given name and filepath
	"""
	config.config_init()
	click.echo(utils.new_app(name, filepath, idfname))
