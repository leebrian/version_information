#!/usr/bin/env python
"""Version information:

IPython extension command for displaying version information about selected
Python modules.
"""

DOCLINES = __doc__.split('\n')

CLASSIFIERS = """\
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 3
Operating System :: MacOS
Operating System :: POSIX
Operating System :: Unix
Operating System :: Microsoft :: Windows
"""

import os
from setuptools import setup

NAME = 'version_information2'
MAJOR = 1
MINOR = 1
MICRO = 0 
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
PACKAGES = ['version_information']
AUTHOR = 'Brian Lee forking  J. Robert Johansson\'s project'
AUTHOR_EMAIL = 'leebrian@prepend.com'
LICENSE = 'CC BY 3.0'
DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = '\n'.join(DOCLINES[2:])
URL = 'https://github.com/leebrian/version_information'
DOWNLOAD_URL = 'https://github.com/leebrian/version_information/archive/v_1.1.0.tar.gz'
PLATFORMS = ['Linux', 'Mac OSX', 'Unix', 'Windows']
KEYWORDS = ['debug','ipython_magic_command','version']
INSTALL_REQUIRES = ['ipython']

def write_version_py(filename=NAME+'/version.py'):
    cnt = """\
# THIS FILE IS GENERATED FROM SETUP.PY
version = '%(version)s'
"""
    with open(filename, 'w') as f:
        f.write(cnt % {'version': VERSION})

write_version_py()

setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    download_url=DOWNLOAD_URL,
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    platforms=PLATFORMS,
    classifiers=CLASSIFIERS
)
