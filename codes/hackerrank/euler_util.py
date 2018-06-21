#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
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


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# https://www.geeksforgeeks.org/orientation-3-ordered-points/
def orientation(p, q, r):
    s1y = q.y - p.y
    s1x = q.x - p.x
    s2y = r.y - q.y
    s2x = r.x - q.x
    # s1y / s1x vs. s2y / s2x
    # < means clockwise
    # = means colinear
    # > means counter-clockwise
    val = s1y * s2x - s2y * s1x
    if val == 0:
        return 'cl'
    elif val < 0:
        return 'cw'
    else:
        return 'cc'


def onsegment(p, r, q):
    return min(p.x, q.x) <= r.x <= max(p.x, q.x) and \
           min(p.y, q.y) <= r.y <= max(p.y, q.y)


# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
def intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 'cl' and onsegment(p1, p2, q1):
        return True
    if o2 == 'cl' and onsegment(p1, q2, q1):
        return True
    if o3 == 'cl' and onsegment(p2, p1, q2):
        return True
    if o4 == 'cl' and onsegment(p2, q1, q2):
        return True
    return False


# compute distance between two gps points.
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # km

    def to_radians(degree):
        return degree * math.pi / 180

    lat_delta = to_radians(lat2 - lat1)
    lon_delta = to_radians(lon2 - lon1)

    lat1 = to_radians(lat1)
    lat2 = to_radians(lat2)

    a = math.sin(lat_delta / 2) * math.sin(lat_delta / 2) + \
        math.cos(lat1) * math.cos(lat2) * math.sin(lon_delta / 2) * math.sin(lon_delta / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c  # in km
    return d


if __name__ == '__main__':
    # check_prime_table()
    # check_qsort()
    # print(haversine_distance(22.520525, 113.93145, 22.530525, 113.94145))
    pass
