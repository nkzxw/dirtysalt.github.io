#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            ans = 1 << 30
            p = 1
            while True:
                p2 = p ** 2
                if p2 > i:
                    break
                p += 1
                ans = min(ans, dp[i - p2] + 1)
            dp[i] = ans
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(34))
    print(sol.numSquares(211))
    print(sol.numSquares(6701))
    print(sol.numSquares(7691))
