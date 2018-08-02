#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# TODO(yan): not working. have some idea.

class Span:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def merge(self, other):
        x0, y0, h0 = self.x, self.y, self.h
        x1, y1, h1 = other.x, other.y, other.h
        out, left, right = None, [], []

        if y1 < y0:
            if x1 >= x0:
                if h0 >= h1:
                    out = Span(x0, y0, h0)
                else:
                    left.append(Span(x0, x1, h0))
                    left.append(Span(x1, y1, h1))
                    out = Span(y1, y0, h0)
            else:
                if h0 >= h1:
                    left.append(Span(x1, x0, h1))
                    out = Span(x0, y0, h0)
                else:
                    left.append(Span(x1, y1, h1))
                    out = Span(y1, y0, h0)
        else:
            if x1 >= x0:
                if h0 >= h1:
                    out = Span(x0, y0, h0)
                    right.append(Span(y0, y1, h1))
                else:
                    left.append(Span(x0, x1, h0))
                    out = Span(x1, y0, h1)
                    right.append(Span(y0, y1, h1))
            else:
                if h0 >= h1:
                    left.append(Span(x1, x0, h1))
                    out = Span(x0, y0, h0)
                    right.append(Span(y0, y1, h1))
                else:
                    left.append(Span(x1, x0, h1))
                    out = Span(x0, y0, h1)
                    right.append(Span(y0, y1, h1))

        left = [x for x in left if x.x < x.y]
        right = [x for x in right if x.x < x.y]
        return out, left, right

    def overlap(self, other):
        return self.y > other.x

    def to_tuple(self):
        return (self.x, self.y, self.h)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __lt__(self, other):
        if self.value.y != other.value.y:
            return self.value.y < other.value.y
        return self.value.x < other.value.x


def insert_span(root, sp):
    if root is None:
        return Node(sp)
    span = root.value
    if span.overlap(sp):
        out, left, right = span.merge(sp)
        span.x = out.x
        span.h = out.h
        for sp2 in left:
            root.left = insert_span(root.left, sp2)
        for sp2 in right:
            root.right = insert_span(root.right, sp2)
    else:
        root.right = insert_span(root.right, sp)
    return root


def list_span(root, res):
    if root is None:
        return
    list_span(root.left, res)
    res.append(root.value)
    list_span(root.right, res)


def merge_span(res):
    if not res:
        return []
    p = res[0]
    out = []
    for i in range(1, len(res)):
        x = res[i]
        if p.y == x.x and p.h == x.h:
            p.y = x.y
        else:
            out.append(p)
            p = x
    out.append(p)
    return out


class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def _buildingOutline(self, buildings):
        # write your code here
        root = None
        for b in buildings:
            span = Span(b[0], b[1], b[2])
            root = insert_span(root, span)
        res = []
        list_span(root, res)
        res = merge_span(res)
        return res

    # lintcode version.
    def buildingOutline(self, buildings):
        buildings.sort(key=lambda x: x[0])
        res = self._buildingOutline(buildings)
        res = [x.to_tuple() for x in res]
        return res

    # leetcode version.
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        res = self._buildingOutline(buildings)
        out = []
        prev = None
        for sp in res:
            if prev is not None and prev.y != sp.x:
                out.append((prev.y, 0))
            out.append((sp.x, sp.h))
            prev = sp
        if prev:
            out.append((prev.y, 0))
        return out


if __name__ == '__main__':
    s = Solution()
    # bs = [[1, 3, 3], [2, 4, 4], [5, 6, 1]]
    # bs = [[1, 100, 20], [2, 99, 19], [3, 98, 18]]
    # print(s.buildingOutline(bs))
    bs = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    # bs = [[2, 9, 10], [3, 7, 15], [5, 12, 12]]
    print(s.buildingOutline(bs))
    print(s.getSkyline(bs))
