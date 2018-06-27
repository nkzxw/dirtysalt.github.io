#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        rounds = minutesToTest / minutesToDie
        while True:
            if (rounds + 1) ** pigs >= buckets:
                break
            pigs += 1
        return pigs


if __name__ == '__main__':
    s = Solution()
    print((s.poorPigs(1000, 15, 60)))
