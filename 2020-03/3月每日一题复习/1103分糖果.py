#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 1103分糖果
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 3:02 下午
#  Description : 顺着题意就万事了


from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        idx = 0
        count = 1
        res = [0] * num_people

        while candies - count > 0:
            res[idx] += count
            idx = (idx + 1) % num_people
            candies -= count
            count += 1

        res[idx] += candies

        return res
