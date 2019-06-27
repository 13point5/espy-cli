import click
from src.app import commands as app_cmds
from src.idf import commands as idf_cmds
from src.utils import config as cfg

@click.group()
def cli():
	"""ESP-IDF Command Line Interface"""
	cfg.config_exists()
	pass


@cli.group()
def app():
	"""Commands related to app"""
	pass


@cli.group()
def idf():
	"""Commands related to idf"""
	pass


@cli.command()
def show():
	"""Show config"""
	cfg.config_disp()


if __name__ == "__main__":
    cli()


app.add_command(app_cmds.create_app, "new")
app.add_command(app_cmds.get_app, "get")
app.add_command(app_cmds.mod_app, "mod")
app.add_command(app_cmds.del_app, "del")


idf.add_command(idf_cmds.create_idf, "new")
idf.add_command(idf_cmds.find_idf, "get")
idf.add_command(idf_cmds.change_idf, "mod")
idf.add_command(idf_cmds.delete_idf, "del")
