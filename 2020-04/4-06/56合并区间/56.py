#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 56.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/6 11:23 上午
#  Description : 太菜了，这题都没思路。。。。


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda x: x[0])  # 以最小坐标排序
        res = []
        pos = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[pos][1]:
                # 两种情况：一种pos的最大大于i的最小并且小于i的最大
                # 另一种是pos的最大大于i的最大
                intervals[pos][1] = max(intervals[i][1], intervals[pos][1])  # merge
            else:  # 当前没有交集，那么以后必然没有交集！
                res.append(intervals[pos])  # 先把结果塞进去
                intervals[pos] = intervals[i]  # 将i位置的坐标赋值到pos，准备进行下一次的判断

        res.append(intervals[pos])  # 推出循环的时候还有一次，否则会漏解
        return res

