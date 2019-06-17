"""
Commands to manage an app
"""

import click
from espy.app import utils
from espy.utils import config, constants, general

@click.command()
@click.option('-n', '--name', type=click.STRING, required=True, help='Name of the app')
@click.option('-f', '--filepath', type=click.STRING, help='Path to directory where app will be created')
@click.option('-idf', '--idfname', type=click.STRING, required=True, help='Name of IDF saved in config')
def create_app(name, filepath, idfname):
	"""
	Create a new app with given name and filepath
	"""
	if not config.config_check(constants.SECTION_IDF):
		general.disp_err("Please add atleast 1 IDF entry to create an app", exit=True)

	click.echo(utils.new_app(name, filepath, idfname))


@click.command()
@click.option('-n', '--name', type=click.STRING, help='Name of the app')
def get_app(name):
	"""
	Get all or specified app from config
	"""
	data = config.get_data(constants.SECTION_APP, "name", name)
	general.disp_json(data, ["name", "filepath", "idf", "idfpath"])
