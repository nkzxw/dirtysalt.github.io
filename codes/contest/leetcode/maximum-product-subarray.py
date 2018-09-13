#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        ans, minv, maxv = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            a, b = minv * nums[i], maxv * nums[i]
            minv = min(a, b, nums[i])
            maxv = max(a, b, nums[i])
            ans = max(ans, maxv)
        return ans


if __name__ == '__main__':
    s = Solution()
    print((s.maxProduct([2, 3, -2, 4])))
    print((s.maxProduct([-2, 0, -1])))
    print((s.maxProduct([3, -1, 4])))
