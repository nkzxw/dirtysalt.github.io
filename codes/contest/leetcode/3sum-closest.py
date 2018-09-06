#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = None
        for i in range(0, len(nums)):
            (k, j) = (i + 1, len(nums) - 1)
            while k < j:
                value = nums[i] + nums[k] + nums[j]
                diff = target - value
                if ans is None or abs(ans - target) > abs(diff):
                    ans = value
                if diff == 0:
                    break
                elif diff > 0:
                    k += 1
                else:
                    j -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
