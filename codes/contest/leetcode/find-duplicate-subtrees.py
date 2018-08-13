#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# TODO(yan): WA

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def match(root, x):
            if root is None and x is None:
                return True
            if root is None or x is None:
                return False
            if root.val != x.val:
                return False
            return match(root.left, x.left) and match(root.right, x.right)

        def find(root, x, res):
            if root != x and match(root, x):
                res.append(root)
            find(root.left, x, res)
            find(root.right, x, res)

        seen = set()
        tree = root
        res = []

        def walk(root):
            if root is None:
                return
            if root not in seen:
                out = []
                find(tree, root, out)
                if out:
                    res.append(root)
                    seen.update(out)
            walk(root.left)
            walk(root.right)

        return res
