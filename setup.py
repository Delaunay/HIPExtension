#!/usr/bin/env python
from setuptools import setup

if __name__ == '__main__':
    setup(
        name='HIPExtension',
        version='0.0.0',
        description='Simple HIPExtension for setuptools',
        author='',
        package_data={
            'hipext': ['*']
        },
        packages=[
            'hipext',
        ],
        setup_requires=['setuptools']
    )
