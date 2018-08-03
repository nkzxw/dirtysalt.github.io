#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from queue import Queue


# TODO(yan): C++ version?

class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """

    def findMinHeightTrees(self, n, edges):
        # Wirte your code here

        adj = []
        for i in range(n):
            adj.append([])
        for (u, v) in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(x, minh):
            queue = Queue()
            visited = [0] * n
            queue.put((x, 1))
            visited[x] = 1
            while not queue.empty():
                v, d = queue.get()
                if d > minh:
                    break
                for v2 in adj[v]:
                    if visited[v2]:
                        continue
                    queue.put((v2, d + 1))
                    visited[v2] = d + 1
            return max(visited)

        out = []
        minh = n
        for x in range(n):
            h = bfs(x, minh)
            out.append((h, x))
            minh = min(minh, h)
        res = [x[1] for x in out if x[0] == minh]
        return res
