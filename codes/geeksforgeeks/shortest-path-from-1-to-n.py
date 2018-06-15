#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# dijkstra
def solve(n):
    INF = 1 << 31
    dist = [INF] * (n + 1)
    dist[1] = 0
    sps = set(range(1, n + 1))

    while True:
        min_dist = INF
        min_node = None
        for v in sps:
            if dist[v] < min_dist:
                min_node = v
                min_dist = dist[v]
        if min_node is None:
            break
        if min_node == n:
            break
        sps.remove(min_node)

        nxts = []
        if (min_node + 1) <= n:
            nxts.append(min_node + 1)
        if min_node * 3 <= n:
            nxts.append(min_node * 3)

        for v2 in nxts:
            dist[v2] = min(dist[v2], min_dist + 1)
    return dist[n]


# dp
def solve_dp(n):
    INF = 1 << 31
    dp = [INF] * (n + 1)
    dp[1] = 0

    def update(v, value):
        if 0 < v <= n:
            dp[v] = min(dp[v], value)

    for i in range(1, n):
        value = dp[i] + 1
        update(i + 1, value)
        update(3 * i, value)
    return dp[n]


# for n in range(1, 1000 + 1):
#     a = solve(n)
#     b = solve_dp(n)
#     if a != b:
#         print('disagree with n = {}, ({}, {})'.format(n, a, b))

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve_dp(n))
