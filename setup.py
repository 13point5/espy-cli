from setuptools import setup, find_packages

setup(
      name="espy-cli",
      version="1.0.0",
	  author="Bharath Sriraam R R",
      author_email="albharath.1305@gmail.com",
	  description="A Command Line application to manage your ESP-IDF projects with ease.",
	  long_description=open('README.md', 'r').read(),
	  long_description_content_type="text/markdown",
      packages=find_packages(exclude=['*__pycache__*', '*espy.egg-info*']),
      install_requires=['click==7.0', 'appdirs==1.4.3', 'terminaltables==3.1.0'],
      entry_points={
        'console_scripts': ['espy = src.cli:cli']
      },
	  url="https://github.com/13point5/espy-cli",
	  classifiers=[
	  	"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux"
    ],
)
