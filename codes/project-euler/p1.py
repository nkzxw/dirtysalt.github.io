#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

xs = [3 * i for i in range(1, 1000 // 3 + 1)]
ys = [5 * i for i in range(1, 1000 // 5 + 1)]
zs = list(set([x for x in xs + ys if x < 1000]))
# print(zs)
print(sum(zs))
