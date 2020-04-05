#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 54.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/5 10:51 下午
#  Description : 小技巧题


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        x1, y1 = 0, 0
        x2, y2 = len(matrix) - 1, len(matrix[0]) - 1
        res = []

        while x1 <= x2 and y1 <= y2:
            res.extend(self._get_edge(matrix, x1, y1, x2, y2))
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1

        return res

    def _get_edge(self, matrix, x1, y1, x2, y2):
        res = []
        if x1 == x2:
            while y1 <= y2:
                res.append(matrix[x1][y1])
                y1 += 1
        elif y1 == y2:
            while x1 <= x2:
                res.append(matrix[x1][y1])
                x1 += 1
        else:
            # step1 lt
            for i in range(y1, y2):
                res.append(matrix[x1][i])
            # step2 rt
            for i in range(x1, x2):
                res.append(matrix[i][y2])
            # step3 rb
            for i in range(y2, y1, -1):
                res.append(matrix[x2][i])
            # step4 lb
            for i in range(x2, x1, -1):
                res.append(matrix[i][y1])

        return res
