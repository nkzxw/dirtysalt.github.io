#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


import functools


def cmp(x, y):
    if x < y: return -1
    if x > y: return 1
    return 0


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=functools.cmp_to_key(lambda x, y: cmp(x.start, y.start) or cmp(x.end, y.end)))
        # print_intervals(intervals)
        res = []
        start, end = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            a, b = intervals[i].start, intervals[i].end
            assert start <= a
            if a <= end:
                end = max(end, b)
            else:
                res.append((start, end))
                start, end = a, b
        res.append((start, end))
        return [Interval(p[0], p[1]) for p in res]
