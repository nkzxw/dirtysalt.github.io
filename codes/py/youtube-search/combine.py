#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import pandas as pd
from pandas import ExcelWriter

parts = ['recipe', 'makeup', 'hairstyle', 'nailart', 'lifehack', 'homedecor', 'diy']
writer = ExcelWriter('keywords-combined.xlsx')
for p in parts:
    df = pd.read_csv(p + '.csv')
    df.to_excel(writer, p)
writer.save()
