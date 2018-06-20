#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n, xs, k):
    s, e = 0, n - 1
    while s != e:
        pivot = xs[s]
        a, b = s, e
        while True:
            while a < b and xs[b] > pivot:
                b -= 1
            if a == b:
                break
            xs[a] = xs[b]
            a += 1
            while a < b and xs[a] < pivot:
                a += 1
            if a == b:
                break
            xs[b] = xs[a]
            b -= 1
            if a == b:
                break
        assert a == b
        xs[a] = pivot
        # print(xs, a)
        if a == k:
            return pivot
        elif a > k:
            e = a - 1
        else:
            s = a + 1
        pass
    return xs[s]


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    k = int(input())
    print(solve(n, xs, k - 1))
