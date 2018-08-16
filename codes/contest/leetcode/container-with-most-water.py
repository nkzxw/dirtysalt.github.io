#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution(object):
    def maxArea(self, height):
        n = len(height)
        hs = [(idx, h) for idx, h in enumerate(height)]
        hs.sort(key=lambda x: x[1])

        left_idx = None
        right_idx = None
        res = 0
        for i in range(n - 1, -1, -1):
            if left_idx is None or hs[i][0] < left_idx:
                left_idx = hs[i][0]
            if right_idx is None or hs[i][0] > right_idx:
                right_idx = hs[i][0]
            area = (right_idx - left_idx) * hs[i][1]
            res = max(res, area)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.maxArea([2, 3, 10, 5, 7, 8, 9]))
