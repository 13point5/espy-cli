import click
import os

@click.group()
def main():
    pass

@main.command()
@click.argument('name', required=True)
@click.option('--filepath', '-fp', help="path to directory where project will be created")
def new(name, filepath):
	""" NAME: name of the project """
	if not filepath: filepath = os.getcwd()
	print(type(name), name)
	print(type(filepath), filepath)


def start():
    main()

if __name__ == "__main__":
    start()
