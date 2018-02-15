#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# import sys
# sys.path.insert(0, '..')

# from . import tasks
# from celery_app import tasks

from . import tasks

for x in range(10):
    r = tasks.add.delay(10, 10)
    print(r.get(propagate=False))
