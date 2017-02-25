#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='alignetpy',
    version='0.1.0',
    description='Python library for online payments with Alignet Gateway.',
    long_description=readme,
    author='Dairon Medina',
    author_email='me@dairon.org',
    url='https://github.com/codeadict/alignetpy',
    packages=['alignetpy'],
    package_dir={'alignetpy':
                 'alignetpy'},
    include_package_data=True,
    install_requires=[
        'pycrypto == 2.6.1',
    ],
    extras_require={
        'testing': ['pytest>=3.0.5'],
    },
    license="MIT",
    zip_safe=True,
    keywords='alignetpy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: E-Commerce',
    ],
)
