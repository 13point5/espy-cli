"""
Commands to manage an app
"""

import click
from src.app import utils
from src.utils import config, constants, general

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
	Get all or specified App from config
	"""
	data = config.get_data(constants.SECTION_APP, "name", name)
	general.disp_json(data, ["name", "filepath", "idf", "idfpath"])


@click.command()
@click.option('-n', '--name', required=True, type=click.STRING, help='Original Name of the app to modify')
def mod_app(name):
	"""
	Modify name or idf of App
	"""
	app_idx = config.get_data(constants.SECTION_APP, "name", name, True)

	option_msgs = [ "Name", "IDF" ]
	click.echo("\nWhat do you wish to modify?")
	for i, o in enumerate(option_msgs):
		msg = "[{}] " + o
		click.echo(msg.format(i+1))
	opt = click.prompt("\nEnter option number (0 for ALL)", type=int)

	option_count = len(option_msgs)
	if opt not in range(option_count + 1):
		general.disp_err("Unknown option", exit=True)

	options = [False] * option_count
	if opt>0:
		options[opt-1] = True
	else:
		options = [True] * option_count

	click.echo(utils.modify_app(app_idx, options, option_msgs))


@click.command()
@click.option('-n', '--name', type=click.STRING, help='Name of the app to delete')
def del_app(name):
	"""
	Delete all or specified App(s)
	"""
	utils.remove_app(name)
