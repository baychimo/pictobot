#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='pictobot',
    version='0.2.0',
    description="A helpful bot showing you pictograms when you're lost in translation",
    long_description=readme,
    author='Jonathan Guitton',
    author_email='jonathan.guitton@gmail.com',
    url='https://github.com/baychimo/pictobot',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
