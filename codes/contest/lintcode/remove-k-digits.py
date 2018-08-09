#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     """
#     @param num: a string
#     @param k: an integer
#     @return: return a string
#     """
#
#     def removeKdigits(self, num, k):
#         # write your code here
#
#         dp = []
#         dp.append(['' for _ in range(k + 1)])
#         dp.append(['' for _ in range(k + 1)])
#
#         now = 0
#         for i in range(len(num)):
#             print(i)
#             ch = num[i]
#             dp[1 - now][0] = dp[now][0] + ch
#             for j in range(1, k + 1):
#                 dp[1 - now][j] = min(dp[now][j - 1], dp[now][j] + ch)
#             now = 1 - now
#
#         s = dp[now][k]
#         idx = 0
#         while idx < len(s) and s[idx] == '0':
#             idx += 1
#         if idx == len(s): return '0'
#         return s[idx:]


if __name__ == '__main__':
    # with open('/Users/dirlt/Downloads/101.in') as fh:
    #     num = eval(fh.readline())
    #     k = eval(fh.readline())
    #     sol = Solution()
    #     print(sol.removeKdigits(num, k))
    sol = Solution()
    print(sol.removeKdigits('1432219', k=3))
