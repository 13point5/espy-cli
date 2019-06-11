import os
import click

def is_dir(dir_path):
	return os.path.isdir(dir_path)


def mk_project(dir_path, dir_name):
	cur_path = os.getcwd()
	if not dir_path:
		dir_path = cur_path

	if not is_dir(dir_path):
		click.echo("The specified directory path does not exist.")
		click.confirm("Countinue to make the directory?", abort=True)
		os.mkdir(dir_path)


	proj_path = os.path.join(dir_path, dir_name)
	if is_dir(proj_path):
		return "Directory already exists"

	os.mkdir(proj_path)
	os.chdir(proj_path)
	os.mkdir("main")

	return "Project created!"
