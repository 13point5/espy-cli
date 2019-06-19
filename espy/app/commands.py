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


@click.command()
@click.option('-n', '--name', required=True, type=click.STRING, help='Original Name of the app to modify')
def mod_app(name):
	"""
	Modify name or idf of app
	"""
	data = config.get_data(constants.SECTION_APP, "name", name)[0]
	
	option_msgs = [ "Name", "IDF" ]
	click.echo("What do you wish to modify?")
	for i, o in enumerate(option_msgs):
		msg = "[{}] " + o
		click.echo(msg.format(i+1))
	opt = click.prompt("\nEnter option number (0 for ALL)", type=int)

	option_count = len(option_msgs) + 1
	if opt not in range(option_count):
		general.disp_err("Unknown option", exit=True)

	options = [False] * option_count
	if opt>0:
		options[opt] = True
	else:
		options = [True] * option_count

	utils.modify_app(data, options, option_msgs)
