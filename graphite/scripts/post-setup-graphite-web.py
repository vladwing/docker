#!/usr/bin/env python
from __future__ import print_function
import os
import random
import string
import sys

import django
django.setup()

from django.contrib.auth.models import User

## Create Superuser
password = ''.join(
    (random.choice(string.letters + string.digits + string.punctuation))
    for x in range(20))

User.objects.create_superuser('admin', 'admin@localhost', password)
print('[graphite-web] Superuser: admin, Password: %s' % (password, ) )
