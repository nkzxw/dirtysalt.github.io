#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        res = [1] * n
        base = 1
        # left -> right
        for i in range(n):
            res[i] *= base
            base *= nums[i]

        base = 1
        # right -> left
        for i in range(n - 1, -1, -1):
            res[i] *= base
            base *= nums[i]

        return res


if __name__ == '__main__':
    s = Solution()
    print((s.productExceptSelf([1, 2, 3, 4])))
