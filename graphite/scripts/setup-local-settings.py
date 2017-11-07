#!/usr/bin/env python
from __future__ import print_function
import os
import random
import string
import sys

from django.utils.crypto import get_random_string

## Add SECRET_KEY to local_settings.py
settings_filename = '/opt/graphite/webapp/graphite/local_settings.py'
secret_key = get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#-_=+')

with open(settings_filename, 'a') as f:
    f.write("SECRET_KEY = '%s'\n" % (secret_key, ))
    if '--debug' in sys.argv:
        f.write('DEBUG = True\n')
