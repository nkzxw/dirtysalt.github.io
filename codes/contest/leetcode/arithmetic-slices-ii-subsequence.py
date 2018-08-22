#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
#

# NOTE(yan): works for non duplicated elements.
# class Solution:
#     def numberOfArithmeticSlices(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#
#         n = len(A)
#         if n == 0: return 0
#
#         vis = [[0] * n for _ in range(n)]
#         ans = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if vis[i][j]:
#                     continue
#
#                 res = []
#                 res.append(i)
#                 res.append(j)
#                 gap = A[j] - A[i]
#                 for k in range(j + 1, n):
#                     if (A[k] - A[res[-1]]) == gap:
#                         res.append(k)
#
#                 count = len(res)
#                 ans += (count - 2) * (count - 1) // 2
#
#                 # print(res)
#                 for k in range(1, len(res)):
#                     vis[res[k - 1]][res[k]] = 1
#         return ans
