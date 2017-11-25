#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from .app import app

# @app.task
@app.task(queue='hipri')
def add(x, y):
    return x + y
