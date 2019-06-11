import click
import os

@click.group()
def main():
    pass

@main.command()
# @click.option('--name', help="Project name.")
# @click.option('--filepath', '-fp', help="Path of directory where the project will live.")
def new(): # name: str, filepath: str
    print(os.getcwd())


def start():
    main()

if __name__ == "__main__":
    start()
