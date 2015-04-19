#! /usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os.path
import sys

def long_description():
    with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
        return f.read()

def install_requires():
    with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
        return [l.split("==")[0] for l in f.readlines() if not l.startswith("#")]

def classifiers():
    if sys.version < '2.2.3':
        return None
    return [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: HTML',
    ]

setup(
    name="mahamoti",
    version="0.1",
    description="Personal life logger",
    long_description=long_description(),
    author="Régis Behmo",
    author_email="regis@behmo.com",
    url="https://github.com/regisb/mahamoti",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    entry_points={'console_scripts': ["mahamoti = mahamoti.run:main"]},
    install_requires=install_requires(),
    license="BSD",
    classifiers=classifiers()
)
