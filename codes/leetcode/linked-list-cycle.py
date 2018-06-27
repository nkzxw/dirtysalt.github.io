#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        x = head
        y = head.__next__
        while x and y:
            if x == y: return True
            x = x.__next__
            y = y.__next__
            if y: y = y.__next__
        return False
