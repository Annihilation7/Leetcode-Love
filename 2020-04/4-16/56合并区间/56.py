#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 56.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/16 8:08 下午
#  Description : 做过了，复习


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])
        res = []

        for i in range(1, len(intervals)):
            if min(intervals[0][1], intervals[i][1]) - max(intervals[0][0], intervals[i][0]) >= 0:
                intervals[0] = [intervals[0][0], max(intervals[0][1], intervals[i][1])]
            else:
                res.append(intervals[0])
                intervals[0] = intervals[i]
        res.append(intervals[0])

        return res
