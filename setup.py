from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in the_factory_suite/__init__.py
from the_factory_suite import __version__ as version

setup(
	name="the_factory_suite",
	version=version,
	description="I&SF ERPNext Customizations",
	author="The Image & Sound Factory NV",
	author_email="tech@image-sound.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
