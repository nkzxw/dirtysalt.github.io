#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self, p0, p1):
        # print nodes_to_list(p0), nodes_to_list(p1)
        dm = ListNode(-1)
        pp = dm
        while p0 and p1:
            if p0.val < p1.val:
                pp.next = p0
                pp = p0
                p0 = p0.__next__
            else:
                pp.next = p1
                pp = p1
                p1 = p1.__next__
        if p0:
            pp.next = p0
        if p1:
            pp.next = p1
        while pp.__next__:
            pp = pp.__next__
        return (dm.__next__, pp)

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = 0
        p = head
        while p:
            n += 1
            p = p.__next__

        dummy = ListNode(-1)
        dummy.next = head
        i = 1
        while (1 << (i - 1)) <= n:
            prev = dummy
            p = dummy.__next__

            while p:
                p0 = p
                for j in range((1 << (i-1)) -1):
                    if not p0.__next__: break
                    p0 = p0.__next__
                p1 = p0.__next__
                p0.next = None

                nextp = None
                if p1:
                    p2 = p1
                    for j in range((1 << (i -1) ) - 1):
                        if not p2.__next__: break
                        p2 = p2.__next__
                    nextp = p2.__next__
                    p2.next = None

                (h, t) = self.merge(p, p1)
                # print nodes_to_list(h)
                prev.next = h
                prev = t
                p = nextp
            i += 1
            prev.next = None
            # print '>>>', nodes_to_list(dummy.next), i
        return dummy.__next__

def list_to_nodes(xs):
    d = ListNode(-1)
    p = d
    for x in xs:
        p.next = ListNode(x)
        p = p.__next__
    p.next = None
    return d.__next__

def nodes_to_list(n):
    xs = []
    while n:
        xs.append(n.val)
        n = n.__next__
    return xs

if __name__ == '__main__':
    s = Solution()
    print(nodes_to_list(s.sortList(list_to_nodes([5, 4,3,1,2,]))))
