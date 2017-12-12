#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import pymongo
from bs4 import BeautifulSoup

ipython = False
try:
    __IPYTHON__
    ipython = True
except NameError:
    pass

if not ipython:
    from gevent import monkey

    monkey.patch_all()

client = pymongo.MongoClient()
db = client['playfm']
TSeries = db['series']
db = client['cache']
TCache = db['playfm']


def get_podcasts_tags():
    rs = TCache.find()
    tags = set()
    for r in rs:
        url = r['_id']
        if url.startswith('https://player.fm/podcasts/'):
            ss = url.split('/')
            tag = ss[-1]
            print('add tag %s' % tag)
            tags.add(tag)
    return tags


def get_series_items():
    rs = TCache.find()
    for r in rs:
        url = r['_id']
        if url.startswith('https://player.fm/series/'):
            yield r


def handle_series(r):
    url = r['_id']
    data = r['data']
    bs = BeautifulSoup(data)
    tags = [x.text for x in bs.select('div.tags > span > a')]
    xs = bs.select('.blatant')
    home = ''
    feed = ''
    for x in xs:
        text = x.text
        if text.find('Series') != -1:
            home = x.attrs.get('href', '')
        if text.find('Feed') != -1:
            feed = x.attrs.get('href', '')
    print(feed)
    data = {
        'tags': tags,
        'home': home,
        'feed': feed
    }
    print('write down data of url = %s' % url)
    TSeries.update({'_id': url}, {'$set': data}, upsert=True)


def update_series_items():
    n_threads = 10
    from gevent.pool import Pool as ThreadPoolExecutor
    pool = ThreadPoolExecutor(n_threads)
    for r in get_series_items():
        pool.spawn(handle_series, r)
    pool.join()

update_series_items()
