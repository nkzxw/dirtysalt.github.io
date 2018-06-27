#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        prev = res
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.__next__
            else:
                prev.next = l2
                l2 = l2.__next__
            prev = prev.__next__

        while l1:
            prev.next = l1
            l1 = l1.__next__
            prev = prev.__next__
        while l2:
            prev.next = l2
            l2 = l2.__next__
            prev = prev.__next__
        prev.next = None
        return res.__next__
