#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        history = [0]
        ans = 0
        acc = 0
        for x in nums:
            acc += x

            l, r = acc - upper, acc - lower
            # history[li..] >= l
            li = bisect.bisect_left(history, l)
            # history[..ri] <= r
            ri = bisect.bisect_right(history, r)
            ans += (ri - li)

            print(history, acc, l, r, ri - li)

            bisect.insort(history, acc)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countRangeSum([-2, 5, -1], -2, 2))
    print(sol.countRangeSum([-1, 1], 0, 0))
