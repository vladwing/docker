#!/usr/bin/env python
from __future__ import print_function
import os
import random
import string
import sys

from django.utils.crypto import get_random_string

SETTINGS_FILE = os.environ.get('SETTINGS_FILE', '/opt/graphite/webapp/graphite/local_settings.py')

def main():
    secret_key = get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#-_=+')
    with open(SETTINGS_FILE, "a+") as f:
        f.write('SECRET_KEY = "' + secret_key + '"\n')

if __name__ == "__main__":
    ## Add SECRET_KEY to local_settings.py
    main()
