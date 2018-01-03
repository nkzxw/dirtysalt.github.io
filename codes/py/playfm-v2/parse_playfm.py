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

def get_series_items():
    rs = TCache.find()
    for r in rs:
        url = r['_id']
        if url.startswith('https://player.fm/series/'):
            yield r

def get_featured_items():
    rs = TCache.find()
    for r in rs:
        url = r['_id']
        if url.startswith('https://player.fm/featured/'):
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
    data = {
        'tags': tags,
        'home': home,
        'feed': feed
    }
    print('write down data of url = %s' % url)
    TSeries.update({'_id': url}, {'$set': data}, upsert=True)

def load_all_series_urls_from_cache():
    print('load series urls from cache')
    rs = TCache.find({}, ('_id',))
    urls = []
    for r in rs:
        url = r['_id']
        if url.find('/series/') != -1:
            urls.append(url)
    return urls

def load_all_series_urls_from_table():
    print('load series urls from table')
    urls = [x['_id'] for x in TSeries.find({}, ('_id'))]
    return urls

# def update_series_items():
#     n_threads = 10
#     from gevent.pool import Pool as ThreadPoolExecutor
#     pool = ThreadPoolExecutor(n_threads)
#     for r in get_series_items():
#         pool.spawn(handle_series, r)
#     pool.join()

def update_series_items():
    urls_cache = load_all_series_urls_from_cache()
    urls_table = load_all_series_urls_from_table()
    diff_urls = list(set(urls_cache) - set(urls_table))
    print('# of diff urls = %d' % len(diff_urls))
    n_threads = 10
    from gevent.pool import Pool as ThreadPoolExecutor
    pool = ThreadPoolExecutor(n_threads)
    for url in diff_urls:
        r = TCache.find_one({'_id': url})
        assert(r is not None)
        pool.spawn(handle_series, r)
    pool.join()


def get_featured_tags_hierarchy():
    def pred(x):
        if not hasattr(x, 'attrs'): return False
        return x.attrs.get('data-toggle', '') == 'popover'

    def parse_single_page(data):
        d = {}
        bs = BeautifulSoup(data)
        tops = [x for x in bs.findAll('a') if pred(x)]
        for t in tops:
            text = t.text
            d[text] = []
            if 'data-content' not in t.attrs:
                continue
            sub_bs = BeautifulSoup(t.attrs['data-content'])
            subs = [x.text for x in sub_bs.select('a')]
            d[text] = subs
        return d

    from collections import defaultdict
    result = defaultdict(list)
    for r in get_featured_items():
        print('handling url = {}'.format(r['_id']))
        data = r['data']
        d = parse_single_page(data)
        for k in d:
            result[k].extend(d[k])
    return result

update_series_items()