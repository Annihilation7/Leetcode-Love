#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 11
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 3:46 下午
#  Description : 双指针的题


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            area = self._get_area(height, l, r)
            if height[l] <= height[r]:
                l += 1  # 宽度缩小的同时，就是尽量让高度变得更高
            else:
                r -= 1
            res = max(res, area)

        return res

    def _get_area(self, height, l, r):
        return min(height[l], height[r]) * (r - l)