#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

setup(name='tap-billy',
      version='0.1',
      description='Singer.io tap for extracting data from the billy API',
      author='Koders',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_dinero'],
      install_requires=[
          'singer-python==0.3.1',
          'backoff==1.3.2',
          'requests==2.12.4',
          'python-dateutil==2.6.0'
      ],
      entry_points='''
          [console_scripts]
          tap-billy=tap_billy:main
      ''',
      packages=['tap_billy']
)
