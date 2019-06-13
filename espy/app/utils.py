import os
import click
from espy.gen_utils import is_dir


def new_app(dir_name, dir_path):
	cur_path = os.getcwd()
	if not dir_path:
		dir_path = cur_path

	if not is_dir(dir_path):
		click.echo("The specified directory path does not exist.")
		click.confirm("Countinue to make the directory?", abort=True)
		os.makedirs(dir_path)

	proj_path = os.path.join(dir_path, dir_name)
	if is_dir(proj_path):
		return "Directory with given project name already exists"

	os.makedirs(os.path.join(proj_path, "main"))
	return "Project created!"
