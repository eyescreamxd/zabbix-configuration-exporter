#!/usr/bin/env python3

from setuptools import setup

setup(
    name='zabbix_configuration_exporter',
    description='Zabbix API wrapper to save configuration to files',
    author='eyescreamxd',
    version='0.2',
    packages=['zabbix_exporter'],
    install_requires=[
        'py-zabbix'
    ],
)
