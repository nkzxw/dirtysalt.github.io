#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices: return 0
#         st = [0] * len(prices)
#         st[-1] = prices[-1]
#         for i in range(len(prices) - 1, 0, -1):
#             st[i - 1] = max(st[i], prices[i - 1])
#
#         v = 0
#         for i in range(0, len(prices)):
#             v = max(v, st[i] - prices[i])
#         return v
#

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        _min = prices[0]
        _max = 0
        for x in prices[1:]:
            diff = x - _min
            if diff > _max:
                _max = diff
            _min = min(_min, x)
        return _max
