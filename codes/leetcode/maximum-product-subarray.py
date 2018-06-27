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

        res = -(1 << 31)
        pos, neg = 0, 0
        for i in range(len(nums)):
            v = nums[i]
            if v == 0:
                pos, neg = 0, 0
                res = max(res, 0)
                continue

            if v > 0:
                pos_tmp, neg_tmp = pos, neg
                pos, neg = v, 0
                if pos_tmp:
                    pos = max(pos, pos_tmp * v)
                if neg_tmp:
                    neg = neg_tmp * v

            else:
                pos_tmp, neg_tmp = pos, neg
                pos, neg = 0, v
                if pos_tmp:
                    neg = min(pos_tmp * v, neg)
                if neg_tmp:
                    pos = neg_tmp * v

            if pos:
                res = max(res, pos)
            if neg:
                res = max(res, neg)
        return res


if __name__ == '__main__':
    s = Solution()
    print((s.maxProduct([2, 3, -2, 4])))
    print((s.maxProduct([-2, 0, -1])))
    print((s.maxProduct([3, -1, 4])))
