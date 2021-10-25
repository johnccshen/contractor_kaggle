import pathlib

import pkg_resources
from setuptools import setup

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='contractore_kaggle',
    version='0.0.1',
    packages=['cell_segmentation'],
    url='',
    license='Apache License 2.0',
    author='ChunChiang',
    author_email='johnccshen@gamail.com',
    description='Contractors Kaggle Competition Playground',
    install_requires=install_requires,
)
