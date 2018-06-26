#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s, e = 0, len(nums) - 1
        while s < e:
            sv = nums[s]
            ev = nums[e]
            if sv < ev:
                return sv
            m = (s + e) // 2
            mv = nums[m]
            if mv >= sv and mv > ev:
                s = m + 1
            else:
                e = m
        assert s == e
        return nums[s]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(s.findMin([4, 5]))
    print(s.findMin([3, 1, 2]))
