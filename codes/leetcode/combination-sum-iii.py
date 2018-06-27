#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import copy


def make_array(base, *dims):
    def _make(base, *dims):
        if len(dims) == 0:
            return base
        v = dims[0]
        res = []
        for _ in range(v):
            res.append(_make(base, *dims[1:]))
        return res

    return _make(base, *dims)


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        cache = {}

        # cache = make_array(None, k + 1, 10, n + 1)

        def solve(k, idx, t):
            if t == 0:
                if k == 0:
                    return [[]]
                return []

            if k == 0:
                return []
            if idx == 0:
                return []

            cache_key = '{}.{}.{}'.format(k, idx, t)
            if cache_key in cache:
                return cache[cache_key]
            # if cache[k][idx][t] is not None:
            #     return cache[k][idx][t]

            res = []
            if idx <= t:
                xs = solve(k - 1, idx - 1, t - idx)
                xs = copy.deepcopy(xs)
                for x in xs:
                    x.append(idx)
                res.extend(xs)
            xs = solve(k, idx - 1, t)
            res.extend(xs)
            cache[cache_key] = res
            # cache[k][idx][t] = res
            return res

        res = solve(k, 9, n)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 10))
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
