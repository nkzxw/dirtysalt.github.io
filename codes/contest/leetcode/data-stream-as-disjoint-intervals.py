#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '({}, {})'.format(self.start, self.end)


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end_map = {}
        self.start_map = {}

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        intv = Interval(val, val)

        end = self.end_map.get(val - 1)
        if end:
            intv.start = end.start
            del self.end_map[val - 1]
            del self.start_map[end.start]

        start = self.start_map.get(val + 1)
        if start:
            intv.end = start.end
            del self.start_map[val + 1]
            del self.end_map[start.end]

        self.end_map[intv.end] = intv
        self.start_map[intv.start] = intv

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        res = list(self.start_map.values())
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

if __name__ == '__main__':
    actions = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
               "getIntervals"]
    values = [[], [49], [], [97], [], [53], [], [5], [], [33], [], [65], [], [62], [], [51], [], [100], [], [38], [],
              [61], [],
              [45], [], [74], [], [27], [], [64], [], [17], [], [36], [], [17], [], [96], [], [12], [], [79], [], [32],
              [], [68],
              [], [90], [], [77], [], [18], [], [39], [], [12], [], [93], [], [9], [], [87], [], [42], [], [60], [],
              [71], [],
              [12], [], [45], [], [55], [], [40], [], [78], [], [81], [], [26], [], [70], [], [61], [], [56], [], [66],
              [], [33],
              [], [7], [], [70], [], [1], [], [11], [], [92], [], [51], [], [90], [], [100], [], [85], [], [80], [],
              [0], [],
              [78], [], [63], [], [42], [], [31], [], [93], [], [41], [], [90], [], [8], [], [24], [], [72], [], [28],
              [], [30],
              [], [18], [], [69], [], [57], [], [11], [], [10], [], [40], [], [65], [], [62], [], [13], [], [38], [],
              [70], [],
              [37], [], [90], [], [15], [], [70], [], [42], [], [69], [], [26], [], [77], [], [70], [], [75], [], [36],
              [], [56],
              [], [11], [], [76], [], [49], [], [40], [], [73], [], [30], [], [37], [], [23], []]
    sol = None
    for (act, val) in zip(actions, values):
        if act == 'SummaryRanges':
            sol = SummaryRanges()
        elif act == 'addNum':
            sol.addNum(val[0])
        elif act == 'getIntervals':
            res = sol.getIntervals()
            print(' '.join(map(str, res)))
