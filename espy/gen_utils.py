import os
import click
from appdirs import *

def is_dir(dir_path):
	return os.path.isdir(dir_path)
