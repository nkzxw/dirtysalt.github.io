#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # assume nums are in hashmap.
        dist = {}
        for n in nums:
            dist[n] = 0

        for n in nums:
            s = n
            # decent nodes and not visited.
            while s in dist and dist[s] == 0:
                s += 1

            # if breaks.
            if s not in dist:
                s -= 1
                dist[s] = 1
                base = 1
            else:  # visited before.
                base = dist[s]

            # update distance backwards.
            while s != n:
                s -= 1
                base += 1
                dist[s] = base

        # print('dist = {}'.format(dist))
        res = max(dist.values())
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
