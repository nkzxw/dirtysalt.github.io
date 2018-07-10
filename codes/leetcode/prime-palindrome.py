#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

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


class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N - 1
        while True:
            n = next_palindrome(n)
            if is_prime(n):
                return n


if __name__ == '__main__':
    s = Solution()
    print(s.primePalindrome(20))
    print(s.primePalindrome(23))
    print(s.primePalindrome(33))
    print(s.primePalindrome(99))
    print(s.primePalindrome(9933))
    print(s.primePalindrome(9999))
    print(next_palindrome(85709140))
    print(s.primePalindrome(85709140))
