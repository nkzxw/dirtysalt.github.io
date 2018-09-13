#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def solve(graph, n):
    inf = 1 << 30
    neg_inf = -inf
    dp = [[[neg_inf] * 2 for _ in range(n)] for _ in range(n)]
    dp[0][0][1] = graph[0][0]

    def get_dp(i, j, d):
        if i < 0 or j < 0:
            return 0
        return dp[i][j][d]

    print('=====')
    for i in range(n):
        print(["%3d" % x for x in graph[i]])

    for i in range(n):
        for j in range(n):
            if (i, j) == (0, 0):
                continue
            res = max(get_dp(i - 1, j, 0), get_dp(i, j - 1, 0)) + graph[i][j]
            dp[i][j][0] = neg_inf if res < 0 else res

            res = max(get_dp(i - 1, j, 1), get_dp(i, j - 1, 1),
                      get_dp(i - 1, j, 0) + get_dp(i, j - 1, 0)) + graph[i][j]
            dp[i][j][1] = neg_inf if res < 0 else res

    print('=====')
    for i in range(n):
        print([x for x in dp[i]])
    ans = dp[n - 1][n - 1][1]
    return ans


n = int(stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n)]
while True:
    a, b, c = [int(x) for x in stdin.readline().split()]
    if not (a and b and c):
        break
    graph[a - 1][b - 1] = c

ans = solve(graph, n)
print(ans)
