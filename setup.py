from setuptools import setup, find_packages

setup(
      # mandatory
      name="espy",
      # mandatory
      version="0.1",
      # mandatory
      author_email="albharath.1305@gmail.com",
      packages=['espy'],
      package_data={},
      install_requires=['click'],
      entry_points={
        'console_scripts': ['espy = espy.cli:start']
      }
)
