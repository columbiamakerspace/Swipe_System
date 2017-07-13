#!/usr/bin/env python

from setuptools import setup
#  from distutils.core import setup

setup(name='SwipeSystem',
      version='1.0',
      description='A card swipe system to manage access to physical machines',
      author='Alex Gaudio',
      author_email='adgaudio@gmail.com',
      url='https://www.github.com/columbiamakerspace/Swipe_System',
      packages=['swipesystem'],
      install_requires=['redis', 'hiredis', 'pynput', 'pyttk'],
      )
