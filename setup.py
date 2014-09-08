from setuptools import setup, find_packages
from ez_setup import use_setuptools
use_setuptools()


PACKAGE = 'namebot'


def _get_requires(filepath):
    with open(filepath) as reqs:
        return [req for req in reqs.read().split('\n') if req]

keywords = ['namebot', 'name generator', 'nlp', 'natural language processing']
description = ('A company/product name generating tool written in Python.'
               'Uses NLTK and diverse wordplay techniques for'
               'sophisticated word generation and ideation')
setup(
    name='namebot',
    version='0.0.1',
    description=description,
    author='Chris Tabor',
    author_email='dxdstudio@gmail.com',
    maintainer='Chris Tabor',
    maintainer_email='dxdstudio@gmail.com',
    url='https://github.com/automotron/namebot',
    keywords=keywords,
    license='MIT',
    packages=find_packages(),
    # install_requires=_get_requires('namebot/requirements.txt'),
    install_requires=['namebot'],
    setup_requires=[
        'setuptools>=0.8',
    ],
    tests_require=[
        'nose',
    ],
    test_suite='tests'
)
