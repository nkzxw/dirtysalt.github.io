#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        n = len(seats)
        if n == 0: return 0
        left = [0] * n
        right = [0] * n

        left[0] = -1
        p = -1
        for i in range(1, n):
            if seats[i - 1] == 1:
                p = i - 1
            left[i] = p

        right[n - 1] = n
        p = n
        for i in range(n - 2, -1, -1):
            if seats[i + 1] == 1:
                p = i + 1
            right[i] = p

        max_dist = -1
        for i in range(0, n):
            if seats[i] == 0:
                if left[i] == -1:
                    dist = right[i] - 0
                elif right[i] == n:
                    dist = (n - 1) - left[i]
                else:
                    dist = min(right[i] - i, i - left[i])
                max_dist = max(max_dist, dist)
        return max_dist
