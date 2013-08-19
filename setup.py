import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'pydsf',
    version = '0.0.1',
    author = 'Nathan Woodbury',
    author_email = 'nathanswoodbury@gmail.com',
    description = ('Addon to Murray\'s Control System Library to add '
                   'functionality for Dynamical Structure Functions.'),
    license = '',
    keywords = 'control systems dynamics',
    url = 'https://github.com/nwoodbury/pydsf',
    packages=['pydsf', 'tests'],
    long_description=read('README.md'),
)
