#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True
