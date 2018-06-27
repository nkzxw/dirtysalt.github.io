#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        prev = res
        dup = None
        while head:
            if (head.val == dup) or \
              (head.__next__ and head.val == head.next.val):
                dup = head.val
            else:
                prev.next = head
                prev = head
            head = head.__next__
        prev.next = None
        return res.__next__
