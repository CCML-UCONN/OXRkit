#!/usr/bin/env python
from distutils.core import setup
import os

def readme():
    with open('README.md') as f:
        return f.read()


scripts = ['tools/ini_oxr','tools/get_oxr']

packages = []
for dirname, dirnames, filenames in os.walk('oxrkit'):
    if '__init__.py' in filenames:
        packages.append(dirname.replace('/', '.'))

setup(name='mlox',
      version='1.0',
      description='Toolkit for OER and ORR analysis',
      long_description=readme(),
      author='Liang Zhang',
      author_email='zhangbright1986@gmail.com',
      packages=packages,
      scripts=scripts,
      )
