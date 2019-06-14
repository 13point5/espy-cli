"""
Commands to manage an app
"""

import click
from espy.app import utils
from espy.utils import config

@click.command()
@click.option('-n', '--name', required=True, type=click.STRING, help='Name of the app')
@click.option('-f', '--filepath', type=click.STRING, help='Path to directory where app will be created')
def create_app(name, filepath):
	"""
	Create a new app with given name and filepath
	"""
	config.config_init()
	click.echo(utils.new_app(name, filepath))
