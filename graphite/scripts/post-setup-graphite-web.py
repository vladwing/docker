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
try:
    User.objects.create_superuser('admin', 'admin@localhost', password)
except:
    u = User.objects.get(username='admin')
    u.set_password(password)
    u.save()
print('[graphite-web] Superuser: admin, Password: %s' % (password, ) )
