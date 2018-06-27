#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        while head:
            p = head
            head = head.__next__

            pp = dummy
            while pp.__next__:
                if p.val > pp.next.val:
                    pp = pp.__next__
                else:
                    break
            p.next = pp.__next__
            pp.next = p
        return dummy.__next__
