#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class PrimeUtil:
    def __init__(self, n):
        self.n = n
        self.table = None

    def build_table(self):
        n = self.n
        table = [1] * (n + 1)
        n2 = PrimeUtil.upper_bound(n)
        for i in range(2, n2):
            if table[i] == 0:
                continue
            for j in range(2, n // i + 1):
                table[i * j] = 0
        self.table = table

    @staticmethod
    def upper_bound(n):
        return min(n - 1, round(n ** 0.5) + 2)

    def is_prime(self, x):
        if not self.table:
            return PrimeUtil.scan(x)
        assert x < len(self.table)
        if x == 1:
            return False
        return True if self.table[x] else False

    @staticmethod
    def scan(n):
        if n == 1:
            return False
        if n == 2:
            return True
        ub = PrimeUtil.upper_bound(n)
        for i in range(2, ub):
            if n % i == 0:
                return False
        return True


def solve(n):
    ub = PrimeUtil.upper_bound(n)
    pu = PrimeUtil(ub)
    pu.build_table()
    for p in range(ub, 1, -1):
        if pu.is_prime(p) and n % p == 0:
            return p
    return n


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
