import click
import os
from .utils import mk_project

@click.group()
def main():
    pass

@main.command()
@click.argument('name', required=True)
@click.option('--filepath', '-fp', help="Path of directory where project will be created")
def new(name, filepath):
	""" NAME: name of the project """
	click.echo(mk_project(filepath, name))


def start():
    main()

if __name__ == "__main__":
    start()
