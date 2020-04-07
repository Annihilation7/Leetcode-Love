#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : main.py
#  Author      : ZhenyuMa
#  Created     : 2020-04-07 21:44
#  Description : 做过不多说了，居然出现在每日一题中了


from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        assert len(matrix) == len(matrix[0]), 'invalid input.'
        lt_x, lt_y = 0, 0
        rb_x, rb_y = len(matrix) - 1, len(matrix[0]) - 1
        while lt_x <= rb_x and lt_y <= rb_y:
            self._reverse_edge(matrix, lt_x, lt_y, rb_x, rb_y)
            lt_x += 1
            lt_y += 1
            rb_x -= 1
            rb_y -= 1

    def _reverse_edge(self, matrix, x1, y1, x2, y2):
        offset = y2 - y1 + 1
        lt = (x1, y1)
        rt = (x1, y2)
        rb = (x2, y2)
        lb = (x2, y1)
        for i in range(offset - 1):
            tmp = matrix[lt[0]][lt[1] + i]
            matrix[lt[0]][lt[1] + i] = matrix[lb[0] - i][lb[1]]
            matrix[lb[0] - i][lb[1]] = matrix[rb[0]][rb[1] - i]
            matrix[rb[0]][rb[1] - i] = matrix[rt[0] + i][rt[1]]
            matrix[rt[0] + i][rt[1]] = tmp

