#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def next_palindrome(x):
    def _next_palindrome(ds):
        n = len(ds)
        s, e = 0, n - 1
        ok = False
        while s <= e:
            if ds[s] != ds[e]:
                if ds[s] > ds[e]:
                    ds[e] = ds[s]
                else:
                    v = ds[s]
                    ds[s] = ds[e] = v + 1
                ok = True
            s += 1
            e -= 1
        if ok: return ds

        m = (n - 1) // 2
        while m >= 0 and ds[m] == 9:
            m -= 1
        if m >= 0:
            # m + 1 .. n - 1 - (m + 1)
            for p in range(m + 1, n - 1 - m):
                ds[p] = 0
            value = ds[m]
            ds[m] = value + 1
            ds[n - 1 - m] = value + 1
            return ds
        ds = [1] + [0] * (n - 1) + [1]
        return ds

    x = [int(c) for c in str(x)]
    x = _next_palindrome(x)
    return int(''.join([str(c) for c in x]))


def list_to_tree(xs):
    stack = []
    root = TreeNode(xs[0])
    stack.append(root)
    i = 1
    while i < len(xs):
        h = stack.pop(0)
        if xs[i]:
            l = TreeNode(xs[i])
            h.left = l
            stack.append(l)
        i += 1

        if i < len(xs):
            if xs[i]:
                r = TreeNode(xs[i])
                h.right = r
                stack.append(r)
            i += 1
    return root
