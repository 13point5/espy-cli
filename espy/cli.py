import click
from espy.app import commands as app_cmds
from espy.idf import commands as idf_cmds

@click.group()
def cli():
	"""ESP-IDF Command Line Interface"""
	pass


@cli.group()
def new():
	"""Create a new App or add IDF path"""
	pass


@cli.group()
def get():
	"""Get Apps or IDF's configured using espy"""
	pass


@cli.group()
def mod():
	"""Modify Apps or IDF's configured using espy"""
	pass

if __name__ == "__main__":
    cli()


new.add_command(app_cmds.create_app, "app")
new.add_command(idf_cmds.create_idf, "idf")


get.add_command(idf_cmds.find_idf, "idf")
