#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Heap:
    def __init__(self):
        self.data = [None]

    def adjust1(self, idx):
        c0 = 2 * idx
        c1 = 2 * idx + 1
        n = len(self.data)
        swap = None

        if c0 < n and not (self.data[idx] < self.data[c0]):
            n0, n1 = self.data[c0], self.data[idx]
            n0.heap_idx = idx
            n1.heap_idx = c0
            self.data[c0], self.data[idx] = n1, n0
            swap = c0

        if c1 < n and not (self.data[idx] < self.data[c1]):
            n0, n1 = self.data[c1], self.data[idx]
            n0.heap_idx = idx
            n1.heap_idx = c1
            self.data[c1], self.data[idx] = n1, n0
            swap = c1

        return swap

    def adjust(self, idx):
        n = len(self.data)
        # down path.
        p = idx
        while p < n:
            swap = self.adjust1(p)
            if swap is None:
                break
            p = swap
        # up path.
        p = idx // 2
        while p:
            swap = self.adjust1(p)
            if swap is None:
                break
            p = p // 2

    def top(self):
        return self.data[1]


class Node:
    def __init__(self, value=None):
        self.value = value
        self.heap_idx = 0

    def __lt__(self, other):
        return self.value > other.value


class DoublyLL:
    def __init__(self):
        dummy = Node()
        self.head = dummy
        self.tail = dummy

    def is_empty(self):
        return self.head is self.tail

    def append_node(self, node):
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def pop_node(self):
        node = self.head.next
        self.head.next = node.next
        if node.next:
            node.next.prev = self.head
        else:
            self.tail = self.head
        return node

    def remove_node(self, node):
        pn = node.prev
        nn = node.next
        pn.next = nn
        if nn:
            nn.prev = pn
        else:
            self.tail = pn


class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """

    def maxSlidingWindow(self, nums, k):
        # write your code here
        if k == 0: return []
        dll = DoublyLL()
        heap = Heap()
        for i in range(k):
            value = nums[i]
            node = Node(value)
            node.heap_idx = i + 1
            dll.append_node(node)
            heap.data.append(node)
            heap.adjust(node.heap_idx)

        res = []
        res.append(heap.top().value)
        for i in range(k, len(nums)):
            old_node = dll.pop_node()
            old_value = old_node.value
            new_value = nums[i]
            new_node = Node(new_value)
            dll.append_node(new_node)

            heap.data[old_node.heap_idx] = new_node
            new_node.heap_idx = old_node.heap_idx
            heap.adjust(new_node.heap_idx)
            res.append(heap.top().value)

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 7, 7, 8]
    k = 3
    print(s.maxSlidingWindow(nums, k))
    nums = [1, 2, 7, 7, 2]
    k = 1
    print(s.maxSlidingWindow(nums, k))

    nums = [1577, 330, 1775, 206, 296, 356, 219, 999, 790, 1435, 1218, 1046, 745, 650, 1199, 1290, 442, 1767, 1098, 521,
            854, 1718, 528, 1011, 1862, 1352, 797, 1453, 779, 1891, 341, 1255, 1892, 98, 978, 1173, 452, 366, 1397, 576,
            1256, 334, 233, 1309, 575, 48, 1308, 1524, 1776, 1514, 541, 1027, 43, 1073, 1136, 83, 1376, 104, 864, 1578,
            57, 1778, 695, 664, 1475, 1025, 341, 248, 687, 848, 1673, 820, 1435, 1622, 1330, 1767, 1189, 828, 1556, 41,
            28, 1283, 462, 373, 1012, 122, 619, 1129, 689, 1610, 616, 452, 1369, 1018, 1784, 528, 683, 346, 1817, 812,
            1905, 1625, 1704, 130, 636, 1731, 1450, 1045, 1352, 809, 429, 991, 1285, 81, 1383, 1406, 1786, 1661, 1059,
            729, 1651, 108, 1608, 114, 484, 471, 962, 1482, 1153, 1238]
    k = 8
    out = s.maxSlidingWindow(nums, k)

    exp = [1775, 1775, 1775, 1435, 1435, 1435, 1435, 1435, 1435, 1435, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1862,
           1862, 1862, 1862, 1862, 1891, 1891, 1891, 1892, 1892, 1892, 1892, 1892, 1892, 1892, 1892, 1397, 1397, 1397,
           1397, 1397, 1397, 1309, 1524, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1514, 1376, 1376, 1578, 1578,
           1778, 1778, 1778, 1778, 1778, 1778, 1778, 1778, 1475, 1673, 1673, 1673, 1673, 1673, 1767, 1767, 1767, 1767,
           1767, 1767, 1767, 1767, 1556, 1556, 1556, 1283, 1283, 1283, 1610, 1610, 1610, 1610, 1610, 1784, 1784, 1784,
           1784, 1817, 1817, 1905, 1905, 1905, 1905, 1905, 1905, 1905, 1905, 1731, 1731, 1731, 1731, 1731, 1450, 1383,
           1406, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1661, 1651, 1651, 1651, 1608, 1608]
    for i in range(len(out)):
        if out[i] != exp[i]:
            print(i, out[i], exp[i])
            break
