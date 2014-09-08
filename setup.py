#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

PACKAGE = 'namebot'

_description = ('A company/product name generating tool written in Python.'
                'Uses NLTK and diverse wordplay techniques for'
                'sophisticated word generation and ideation')
setup(
    name='namebot',
    version='0.0.1',
    description=_description,
    author='Chris Tabor',
    author_email='dxdstudio@gmail.com',
    maintainer='Chris Tabor',
    maintainer_email='dxdstudio@gmail.com',
    url='https://github.com/automotron/namebot',
    keywords=['namebot', 'name generator', 'nlp'],
    license='MIT',
    setup_requires=[
        'setuptools>=0.8',
    ],
    tests_require=[
        'nose',
    ],
    test_suite='tests'
)
