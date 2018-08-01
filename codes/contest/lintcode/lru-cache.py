#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# 这个doubly linked list有点难写，最好创建一个dummy node.
class Root:
    def __init__(self):
        dummy = Node()
        self.head = dummy
        self.tail = dummy
        self.count = 0

    def remove_node(self, node):
        self.count -= 1
        pn = node.prev
        nn = node.next
        if nn is None:
            pn.next = None
            self.tail = pn
        else:
            pn.next = nn
            nn.prev = pn

    def insert_node(self, node):
        self.count += 1
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        if head_next is not None:
            head_next.prev = node
        else:
            self.tail = node

    def dump(self):
        prev = None
        head = self.head
        values = []
        while head:
            assert head.prev is prev
            values.append('({}, {})'.format(head.key, head.value))
            prev = head
            head = head.next
        assert prev is self.tail
        return values


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.node_list = Root()
        self.node_map = {}
        self.cap = capacity

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        node = self.node_map.get(key)
        if node is None:
            return -1
        self.node_list.remove_node(node)
        self.node_list.insert_node(node)
        return node.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        node = self.node_map.get(key)
        if node is not None:
            node.value = value
            self.node_list.remove_node(node)
            self.node_list.insert_node(node)
            return

        # eviction.
        if len(self.node_map) == self.cap:
            tail = self.node_list.tail
            del self.node_map[tail.key]
            self.node_list.remove_node(tail)

        node = Node(key, value)
        self.node_map[key] = node
        self.node_list.insert_node(node)
