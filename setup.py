from glob import glob
from itertools import chain
import os
import os.path as pth
import re
from setuptools import setup, find_packages
from unittest import TestLoader
from pprint import pprint

PACKAGE_NAME    = 'scistyles'
DESCRIPTION     = 'Matplotlib stylesheets and figure design tools.'
URL             = 'https://github.com/spalato/scistyles'
DOWNLOAD_URL    = ''
BASE_PACKAGE    = 'src/scistyles'


base_path = os.path.dirname(__file__)

with open(os.path.join(base_path, BASE_PACKAGE, '__init__.py')) as f:
    module_content = f.read()
    VERSION = re.compile(r'.*__version__ = \'(.*?)\'', re.S).match(module_content).group(1)
    LICENSE = re.compile(r'.*__license__ = \'(.*?)\'', re.S).match(module_content).group(1)
    AUTHOR = re.compile(r'.*__author__ = \'(.*?)\'', re.S).match(module_content).group(1)
    AUTHOR_EMAIL = re.compile(r'.*__email__ = \'(.*?)\'', re.S).match(module_content).group(1)

with open('README.md') as f:
    README = f.read()

with open('requirements.txt') as f:
    REQUIREMENTS = [line for line in f.read().split('\n') if len(line.strip())]

exclude = {'exclude': []}#['external*', 'docs', '*cache']}

if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        description=DESCRIPTION,
        long_description=README,
        license=LICENSE,
        url=URL,
        download_url=DOWNLOAD_URL,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=AUTHOR,
        maintainer_email=AUTHOR_EMAIL,
        install_requires=REQUIREMENTS,
        keywords=[],
        packages=find_packages("src", **exclude),
        package_dir={'': 'src'},
        py_modules = [],
        include_package_data=True,
        zip_safe=False,
        # list of possible classifiers:
        #  https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            "Framework :: Matplotlib",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Topic :: Scientific/Engineering :: Visualization",
        ]
    )