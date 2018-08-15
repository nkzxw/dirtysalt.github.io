#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 3
        maxs = [None] * k

        for v in nums:
            for i in range(k):
                if maxs[i] is None or v > maxs[i]:
                    for j in range(k - 1, i, -1):
                        maxs[j] = maxs[j - 1]
                    maxs[i] = v
                    break
                elif v == maxs[i]:
                    break

        if maxs[k - 1] is None:
            return maxs[0]
        return maxs[k - 1]
