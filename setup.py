import os
import sys

from setuptools import setup, Command
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """
    Integrate pytest into setup.py
    """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def read(fname):
    """
    Utility function to read the README file.
    """
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
    packages=['pydsf'],
    long_description=read('README.md'),
    tests_require=['pytest'],
    cmdclass={'test': PyTest}
)
