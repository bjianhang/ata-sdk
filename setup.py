#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('ata_submit/version.py', 'rb') as f:
    version = str(
        ast.literal_eval(
            _version_re.search(f.read().decode('utf-8')).group(1)))

setup(
    name="ata_submit",
    version=version,
    url='',
    long_description=open('README.md').read(),
    packages=find_packages(),
)
