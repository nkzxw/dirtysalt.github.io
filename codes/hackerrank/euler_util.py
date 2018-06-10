#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


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
