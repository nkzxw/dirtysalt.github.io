#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        seen = {}
        dummy = RandomListNode(0)
        
        p = dummy
        t = head        
        while t:
            t2 = RandomListNode(t.label)
            p.next = t2
            p = t2
            seen[t] = t2
            t = t.__next__

        t = head
        p = dummy.__next__
        while t:
            r = t.random
            r2 = seen[r] if r else None
            p.random = r2
            t = t.__next__
            p = p.__next__

        return dummy.__next__
