#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s, e = 0, len(nums) - 1
        INT_MIN = -(1 << 63)
        while s <= e:
            m = (s + e) // 2
            l = nums[m - 1] if m > 0 else INT_MIN
            r = nums[m + 1] if m < len(nums) - 1 else INT_MIN
            if nums[m] > l and nums[m] > r:
                return m
            elif nums[m] < l:
                e = m - 1
            else:
                s = m + 1
        return -1
