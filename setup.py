import re
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bahrain_vat/__init__.py
# without importing the package (avoids build-time ModuleNotFoundError)
with open('bahrain_vat/__init__.py', 'r') as f:
	version = re.search(
		r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
		f.read(),
		re.MULTILINE
	).group(1)

setup(
	name='bahrain_vat',
	version=version,
	description='BAHRAIN VAT Management and Reporting',
	author='ERPGulf',
	author_email='support@erpgulf.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
