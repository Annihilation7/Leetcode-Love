#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 937.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/12 12:11 上午
#  Description : 写一个排序函数？


from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self._sort_func)

    def _sort_func(self, log):
        flag, name = log.split(' ', 1)
        if name[0].islower():
            return 0, name, flag  # 规定的排序的优先级
        return 1, 0, 0  # 0，0两个数字相等相当于规定了按照原先的顺序，厉害了！
