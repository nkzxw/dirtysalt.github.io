#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


def cmp(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    return 0


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        xs = [(v, idx) for (idx, v) in enumerate(nums)]
        xs.sort(key=functools.cmp_to_key(lambda x, y: cmp(x[0], y[0]) or cmp(x[1], y[1])))
        print(xs)
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                if (xs[j][0] - xs[i][0]) <= t:
                    if abs(xs[j][1] - xs[i][1]) <= k:
                        return True
                else:
                    break
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
    print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
    print(s.containsNearbyAlmostDuplicate([0, 10, 22, 15, 0, 5, 22, 12, 1, 5], 3, 3))
    print(s.containsNearbyAlmostDuplicate([1, 3, 6, 2], 1, 2))
