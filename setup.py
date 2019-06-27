from setuptools import setup, find_packages

setup(
      name="espy-cli",
      version="0.1",
	  author="Bharath Sriraam R R",
      author_email="albharath.1305@gmail.com",
	  description="A Command Line application to manage your ESP-IDF projects with ease.",
	  long_description=open('README.md').read(),
      packages=find_packages(exclude=['*__pycache__*', '*espy.egg-info*']),
      package_data={},
      install_requires=['click', 'appdirs', 'terminaltables'],
      entry_points={
        'console_scripts': ['espy = espy.cli:cli']
      },
	  url="https://github.com/13point5/espy-cli"
)
