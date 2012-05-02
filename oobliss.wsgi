#!/usr/bin/env python

import os
import sys

# This is all you have to update. Assuming that the project is found in the
# same directory as me!
PROJECT = 'oob'


# Change me to match your app's settings module
DJANGO_SETTINGS_MODULE = PROJECT + '.settings'
ABSPATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(ABSPATH)
PROJECT_DIR = os.path.join(DIRNAME, PROJECT)
print PROJECT_DIR
ACTIVATE_THIS = os.path.join(DIRNAME, 'bin/activate_this.py')

# Ref: http://code.google.com/p/modwsgi/wiki/VirtualEnvironments
sys.path.append(DIRNAME)
execfile(ACTIVATE_THIS, dict(__file__=ACTIVATE_THIS))

# DO NOT TOUCH
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
