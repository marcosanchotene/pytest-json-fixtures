#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-json-fixtures',
    version='0.2.0',
    author='Marco Sanchotene',
    author_email='marco@pontograu.com',
    maintainer='Marco Sanchotene',
    maintainer_email='marco@pontograu.com',
    license='MIT',
    url='https://github.com/marcosanchotene/pytest-json-fixtures',
    description='JSON output for the --fixtures flag',
    long_description=read('README.rst'),
    py_modules=['pytest_json_fixtures'],
    python_requires='>=3.5',
    install_requires=['pytest>=7.1.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'json-fixtures = pytest_json_fixtures',
        ],
    },
)
