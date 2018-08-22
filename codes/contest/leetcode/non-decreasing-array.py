#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# NOTE(yan): 这题目要考虑到各种cases.

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                # assume nums[i] == nums[i-1]
                # or nums[i-1] == nums[i]
                if ((i + 1) >= len(nums) or nums[i - 1] <= nums[i + 1]) or \
                        ((i - 2) < 0 or nums[i] >= nums[i - 2]):
                    count += 1
                    if count == 2:
                        return False
                else:
                    return False
        return True
