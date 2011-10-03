#!/usr/bin/python

import sys, os
from setuptools import setup
from setuptools import find_packages

__author__ = 'Matthew Hokanson <m@h0ke.com>'
__version__ = '0.1.0'

setup(
    name = 'pynecone',
    version = __version__,

    install_requires = ['simplejson', 'urllib', 'urllib2'],

    author = 'Matthew Hokanson',
    author_email = 'm@h0ke.com',
    license = 'MIT License',
    url = 'http://github.com/h0ke/pynecone/tree/master',
    keywords = 'forrst api python wrapper pynecone',
    description = 'Pynecone is a Python client that wraps the Forrst API.',
    long_description = open('README.markdown').read(),
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet'
    ]
)
