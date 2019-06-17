import click
from espy.app import commands as app_cmds
from espy.idf import commands as idf_cmds
from espy.utils import config

@click.group()
def cli():
	"""ESP-IDF Command Line Interface"""
	config.config_exists()
	pass


@cli.group()
def app():
	"""Commands related to app"""
	pass


@cli.group()
def idf():
	"""Commands related to app"""
	pass


if __name__ == "__main__":
    cli()


app.add_command(app_cmds.create_app, "new")
app.add_command(app_cmds.get_app, "get")


idf.add_command(idf_cmds.create_idf, "new")
idf.add_command(idf_cmds.find_idf, "get")
idf.add_command(idf_cmds.delete_idf, "del")
