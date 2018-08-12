#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        def ch2idx(c):
            return ord(c) - ord('a')

        counter = [0] * 26
        for c in s:
            idx = ch2idx(c)
            counter[idx] += 1

        preps = []
        for word in ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
            vec = []
            for c in word:
                vec.append(ch2idx(c))
            preps.append(vec)

        def remove_chars(c, digit):
            idx = ch2idx(c)
            prep = preps[digit]
            cnt = counter[idx]
            for idx in prep:
                counter[idx] -= cnt
            return str(digit) * cnt

        res = ''
        res += remove_chars('z', 0)
        res += remove_chars('x', 6)
        res += remove_chars('w', 2)
        res += remove_chars('u', 4)
        res += remove_chars('g', 8)
        res += remove_chars('o', 1)
        res += remove_chars('h', 3)
        res += remove_chars('f', 5)
        res += remove_chars('v', 7)
        res += remove_chars('i', 9)
        res = list(res)
        res.sort()
        res = ''.join(res)
        return res
