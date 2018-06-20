#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import random

import numpy as np


def prime_build_table(n):
    table = [1] * (n + 1)
    table[1] = 0
    n2 = prime_upper_bound(n)
    for i in range(2, n2):
        if table[i] == 0:
            continue
        for j in range(i, n // i + 1):
            table[i * j] = 0
    return table


def prime_upper_bound(n):
    return min(n - 1, round(n ** 0.5) + 2)


def check_prime_table():
    print('check prime table ...')
    n = 10 ** 6
    table = prime_build_table(n)
    for x in range(2, len(table)):
        exp = is_prime(x)
        val = bool(table[x])
        if exp != val:
            print('failed at {}. (exp = {}, val = {})'.format(x, exp, val))
            break
    print('PASSED!!!')


def factor_build_table(n):
    table = []
    for i in range(n + 1):
        table.append([])
    n2 = prime_upper_bound(n)
    for i in range(2, n2):
        for j in range(i, n // i + 1):
            v = i * j
            table[v].append(i)
    return table


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    ub = prime_upper_bound(n)
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while True:
        c = a % b
        if c == 0:
            return b
        a, b = b, c


def lcm(a, b):
    c = gcd(a, b)
    return a * b // c


def miller_rabin(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


def qsort_pivot(xs, s, e):
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
    return a


def qsort_range(xs, s, e):
    if s >= e:
        return
    p = qsort_pivot(xs, s, e)
    qsort_range(xs, s, p - 1)
    qsort_range(xs, p + 1, e)


def qsort(xs):
    n = len(xs)
    qsort_range(xs, 0, n - 1)


def check_qsort():
    print('check qsort ...')
    n = 10 ** 3
    t = 1000
    for _ in range(t):
        xs = np.random.randint(-10 ** 6, 10 ** 6, n)
        xs2 = xs.copy()
        qsort(xs)
        xs2.sort()
        assert np.all(np.array(xs) == xs2)
    print('PASSED!!!')


if __name__ == '__main__':
    # check_prime_table()
    # check_qsort()
    pass
