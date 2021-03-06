#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from __future__ import absolute_import

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

from checkdmarc import __version__

desc = "A Python module and command line parser for SPF and DMARC records"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='checkdmarc',

    # Versions should comply with PEP440.  Fr a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description=desc,
    long_description=long_description,

    # The project's main homepage.
    url='https://domainaware.github.io/checkdmarc',

    # Author details
    author='Sean Whalen',
    author_email='whalenster@gmail.com',

    # Choose your license
    license='Apache 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        "Intended Audience :: Information Technology",
        'Operating System :: OS Independent',


        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

    ],

    # What does your project relate to?
    keywords='DNS, SPF, DMARC',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),


    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["checkdmarc"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['dnspython>=2.0.0', 'expiringdict>=1.1.4',
                      'pyleri>=1.3.2', 'publicsuffix2>=2.20191221',
                      'requests>=2.25.0',
                      'timeout-decorator>=0.4.1'],

    entry_points={
        'console_scripts': ['checkdmarc=checkdmarc:_main'],
    }
)
