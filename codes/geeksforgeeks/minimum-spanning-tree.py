#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n, e, xs):
    edges = []
    for i in range(n):
        edges.append([])
    for i in range(e):
        a = xs[3 * i] - 1
        b = xs[3 * i + 1] - 1
        c = xs[3 * i + 2]
        edges[a].append((b, c))
        edges[b].append((a, c))
    return _solve(edges, n)


def _solve(edges, n):
    inf = 1 << 31
    dist = [(inf, -1, -1)] * n
    cut_nodes = set(range(n))
    mst_edges = []
    # (edge value, start node, end node)
    dist[0] = (0, -1, -1)
    while cut_nodes:
        min_dist = inf
        min_node = None
        for v in cut_nodes:
            if dist[v][0] < min_dist:
                min_dist = dist[v][0]
                min_node = v
        if min_node is None:
            break
        assert min_node is not None
        cut_nodes.remove(min_node)
        mst_edges.append(dist[min_node])

        for v, val in edges[min_node]:
            if v not in cut_nodes:
                continue
            if val < dist[v][0]:
                dist[v] = (val, min_node, v)
    # print(mst_edges)
    res = sum([x[0] for x in mst_edges])
    return res


def spanningTree(graph, n, e):
    edges = []
    for i in range(n):
        nxts = []
        for j in range(n):
            if graph[i][j]:
                nxts.append((j, graph[i][j]))
        edges.append(nxts)
    return _solve(edges, n)


t = int(input())
for _ in range(t):
    n, e = [int(x) for x in input().rstrip().split()]
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(n, e, xs))
