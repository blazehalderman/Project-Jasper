# -*- UTF-8 -*-

# initialize global variables, imports

# -- setup for battelship game --

import os
from setuptools import setup, find_packages

setup(
    name='Battleship-Python',
    version='0.0.1',
    description='A Python Battleship AI',
    long_description='Battleship AI that learns over time using deep learning',
    author='Blaze Halderman',
    author_email='blazehalderman@gmail.com',
    url='https://github.com/blazehalderman/Project-Jasper',
    license='MIT',
    packages=find_packages('battleship_ai', 'tests')
)