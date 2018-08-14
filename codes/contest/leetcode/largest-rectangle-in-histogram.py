#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        ps = []
        hs = []
        res = 0
        for i in range(len(heights)):
            h = heights[i]
            idx = i
            while hs and h < hs[-1]:
                out = (i - ps[-1]) * hs[-1]
                idx = ps[-1]
                res = max(res, out)
                ps.pop()
                hs.pop()
            hs.append(h)
            ps.append(idx)

        i = len(heights)
        while hs:
            out = (i - ps[-1]) * hs[-1]
            res = max(res, out)
            ps.pop()
            hs.pop()
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([2, 1, 2]))
