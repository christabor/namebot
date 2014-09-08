from setuptools import setup
from ez_setup import use_setuptools
use_setuptools()


PACKAGE = 'namebot'


def _get_requires(filepath):
    with open(filepath) as reqs:
        return [req for req in reqs.read().split('\n') if req]


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
    packages=['namebot', 'namebot.tests'],
    install_requires=_get_requires('namebot/requirements.txt'),
    setup_requires=[
        'setuptools>=0.8',
    ],
    tests_require=[
        'nose',
    ],
    test_suite='tests'
)
