#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


def bf_next_palindrome(x):
    while True:
        x += 1
        if is_palindrome(x):
            return x


def next_palindrome(x):
    def _find(x):
        while True:
            if is_palindrome(x):
                return x
            ds = list(str(x))
            n = len(ds)
            s, e = 0, n - 1
            carry = 0
            while s <= e:
                if ds[s] > ds[e]:
                    ds[e] = ds[s]
                elif ds[s] < ds[e]:
                    carry = ord('9') - ord(ds[e]) + 1
                    carry *= (10 ** s)
                    break
                s += 1
                e -= 1
            x = int(''.join(ds))
            x += carry

    if is_palindrome(x):
        x = _find(x + 1)
    else:
        x = _find(x)
    return x


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


def check_next_palindrome():
    N = 10000
    for x in range(1, N):
        a = next_palindrome(x)
        b = bf_next_palindrome(x)
        if a != b:
            print('x = {}, a = {}, b = {}'.format(x, a, b))


if __name__ == '__main__':
    check_next_palindrome()
