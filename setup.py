import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()


PACKAGE = 'namebot'


def _get_requires(filepath):
    path = '{}/{}'.format(os.path.abspath(os.path.dirname(__file__)), filepath)
    with open(path) as reqs:
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
    license='Apache License 2.0',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=_get_requires('requirements.txt'),
    setup_requires=[
        'setuptools>=0.8',
    ],
    tests_require=[
        'nose',
    ],
    test_suite='tests',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Utilities',
    ]
)
