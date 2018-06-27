#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        
        x = head
        cnt = 0
        while x:
            cnt +=1
            x = x.__next__
            
        prev = dummy
        for i in range(cnt - n):
            prev = prev.__next__
        n = prev.__next__
        nn = n.__next__
        prev.next = nn

        return dummy.__next__
