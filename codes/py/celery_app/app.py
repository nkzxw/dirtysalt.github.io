#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from celery import Celery

app = Celery('my_celery_app', broker = 'redis://localhost:6379/1',
             backend = 'redis://localhost:6379/2',
             task_serializer='json',
             result_serializer='json',
             enable_utc=True,
             include = ['celery_app.tasks'])

app.conf.update(result_expires = 3600)
app.config_from_object('celery_app.config')

app.conf.update(
    task_routes = {
        'celery_app.tasks.add': {'queue': 'hipri'}
    }
)

if __name__ == '__main__':
    print(app.conf.timezone)
    print(app.conf.humanize(with_defaults=False, censored=False))
    # app.start()
