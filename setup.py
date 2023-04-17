from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nesscale_website/__init__.py
from nesscale_website import __version__ as version

setup(
	name="nesscale_website",
	version=version,
	description="Nesscale Website",
	author="Nesscale Solutions Private Limited",
	author_email="info@nesscale.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
