#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# TODO(yan): 使用heap的方法来动态更新权重

class Heap:
    def __init__(self, cap):
        self.data = [None]
        self.cap = cap

    def adjust(self, idx):
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

    def walk_down(self, idx):
        n = len(self.data)
        while idx < n:
            swap = self.adjust(idx)
            if swap is None:
                break
            idx = swap

    def walk_up(self, idx):
        while idx:
            self.adjust(idx)
            idx = idx // 2

    def append(self, node):
        evicted = None
        n = len(self.data)
        if (n - 1) == self.cap:
            evicted = self.data[1]
            node.heap_idx = 1
            self.data[1] = node
            self.walk_down(1)
        else:
            node.heap_idx = n
            self.data.append(node)
            self.walk_up(n)
        return evicted

    def down(self, node):
        self.walk_down(node.heap_idx)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.op_count = 0
        self.op_idx = 0
        self.heap_idx = 0

    def inc_count(self, op_idx):
        self.op_count += 1
        self.op_idx = op_idx

    def __lt__(self, other):
        if self.op_count != other.op_count:
            return self.op_count < other.op_count
        return self.op_idx < other.op_idx


class LFUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.node_map = dict()
        self.node_heap = Heap(capacity)
        self.global_op_idx = 0

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def inc_global_op_idx(self):
        ts = self.global_op_idx
        self.global_op_idx += 1
        return ts

    def set(self, key, value):
        # write your code here
        op_idx = self.inc_global_op_idx()
        node = self.node_map.get(key)
        if node is not None:
            node.inc_count(op_idx)
            node.value = value
            self.node_heap.down(node)
            return

        node = Node(key, value)
        node.inc_count(op_idx)
        evicted = self.node_heap.append(node)
        if evicted:
            del self.node_map[evicted.key]
        self.node_map[node.key] = node

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        ts = self.inc_global_op_idx()
        # write your code here
        node = self.node_map.get(key)
        if node is not None:
            node.inc_count(ts)
            self.node_heap.down(node)
            return node.value
        return -1
