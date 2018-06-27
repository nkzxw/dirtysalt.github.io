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
        if not head: return head
        res = head
        prev = res
        head = head.__next__
        while head:
            if head.val != prev.val:
                prev.next = head
                prev = head
            head = head.__next__
        prev.next = None
        return res
