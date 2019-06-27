import os
from appdirs import user_config_dir


SECTION_IDF = 'IDFs'
SECTION_APP = 'Apps'

CONFIG_DIR = user_config_dir("espy-cli")
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')
