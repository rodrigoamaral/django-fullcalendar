#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fullcalendar',
    version='0.1',
    packages=['fullcalendar', 'fullcalendar.templatetags',],
    include_package_data=True,
    license='MIT License',  # example license
    install_requires=REQUIREMENTS,
    description='FullCalendar jQuery plugin integration with Django.',
    long_description=README,
    url='http://github.com/rodrigoamaral/django-fullcalendar',
    author='Rodrigo Amaral',
    author_email='rodrigo@rodrigoamaral.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)