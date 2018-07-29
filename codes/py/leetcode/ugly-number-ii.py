#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import heapq as hq


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1: return 1
        n -= 1
        primes = (2, 3, 5)
        ways = [[x] for x in list(primes)]
        seen = set(primes)

        for _ in range(n - 1):
            min_idx = 0
            min_value = ways[0][0]
            for i in range(1, len(ways)):
                if ways[i][0] < min_value:
                    min_value = ways[i][0]
                    min_idx = i

            hq.heappop(ways[min_idx])
            for p in primes[min_idx:]:
                nv = min_value * p
                if nv not in seen:
                    hq.heappush(ways[min_idx], nv)
                    seen.add(nv)

        # print(ways)
        return min([x[0] for x in ways])


if __name__ == '__main__':
    s = Solution()
    print((s.nthUglyNumber(2)))
