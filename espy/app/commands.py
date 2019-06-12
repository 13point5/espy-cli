"""
Commands to manage an app
"""

import click
from espy.app import utils

@click.command()
@click.option('-n', '--name', type=click.STRING, help='Name of the app')
@click.option('-f', '--filepath', type=click.STRING, help='Path to directory where app will be created')
def create_app(name, filepath):
	"""
	Create a new app with given name and filepath
	"""
	if not name:
		click.echo('Example usage:\n' +
					'Create an app in current directory: espy new app -n hello_world\n' +
					'Specify the directory for the app:  espy new app -n hello_world -f "/home/<user>/projects/"')

	else:
		click.echo(utils.new_app(name, filepath))
