#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import random


def prime_build_table(n):
    table = [1] * (n + 1)
    table[1] = 0
    n2 = prime_upper_bound(n)
    for i in range(2, n2):
        if table[i] == 0:
            continue
        for j in range(2, n // i + 1):
            table[i * j] = 0
    return table


def prime_upper_bound(n):
    return min(n - 1, round(n ** 0.5) + 2)


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
