# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:19:51 2016

@author: fred
"""

from setuptools import setup

setup(
    name='fortune21',
    version='0.1',
    py_modules=['fortune21'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fortune21=fortune21:cli
    ''',
)
