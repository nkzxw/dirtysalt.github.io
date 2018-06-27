#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        res = 0

        # choose 0th, not choose 1th.
        # 那么不能选择最后一个item.
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(n):
            for k in (2, 3):
                v = i + k
                if v >= (n - 1):
                    continue
                dp[v] = max(dp[v], dp[i] + nums[v])
        res = max(res, max(dp[-3:]))

        # not choose 0th, choose 1th.
        # 那么可以选择最后一个item.
        dp = [0] * n
        dp[1] = nums[1]
        for i in range(n):
            for k in (2, 3):
                v = i + k
                if v >= n:
                    continue
                dp[v] = max(dp[v], dp[i] + nums[v])
        res = max(res, max(dp[-2:]))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 3, 2]))
    print(s.rob([1, 2, 3, 1]))
