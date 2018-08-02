#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import defaultdict


class Solution:
    """
    @param edges: a directed graph where each edge is represented by a tuple
    @return: the number of edges
    """

    def balanceGraph(self, edges):
        # Write your code here

        nodes = defaultdict(int)
        for (u, v, w) in edges:
            nodes[u] -= w
            nodes[v] += w

        p0 = []
        p1 = []
        for k, v in nodes.items():
            if v > 0:
                p0.append(v)
            elif v < 0:
                p1.append(-v)

        p0.sort()
        p1.sort()

        # 优先匹配相同的
        def compress(p0, p1):
            n = len(p0)
            x0, x1 = [], []
            idx0, idx1 = 0, 0
            res = 0
            while idx0 < n and idx1 < n:
                if p0[idx0] == p1[idx1]:
                    res += 1
                    idx0 += 1
                    idx1 += 1
                elif p0[idx0] > p1[idx1]:
                    x1.append(p1[idx1])
                    idx1 += 1
                else:
                    x0.append(p0[idx0])
                    idx0 += 1
            x0.extend(p0[idx0:])
            x1.extend(p1[idx1:])
            return res, x0, x1

        # 然后使用贪心算法
        res, p0, p1 = compress(p0, p1)
        n = len(p0)
        idx0, idx1 = 0, 0
        while idx0 < n:
            if p0[idx0] == p1[idx1]:
                idx0 += 1
                idx1 += 1
            elif p0[idx0] > p1[idx1]:
                p0[idx0] -= p1[idx1]
                idx1 += 1
            else:
                p1[idx1] -= p0[idx0]
                idx0 += 1
            res += 1
        return res
