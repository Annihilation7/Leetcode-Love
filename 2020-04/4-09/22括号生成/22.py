#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 22.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/9 8:51 下午
#  Description : 一道dfs + 剪枝


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.helper(n, n, '')
        return self.res

    def helper(self, left_residual, right_residual, cur_res):
        if left_residual == 0 and right_residual == 0:
            self.res.append(cur_res)
            return

        if left_residual > right_residual:
            return

        if left_residual > 0:
            self.helper(left_residual - 1, right_residual, cur_res + '(')
        if right_residual > 0:
            self.helper(left_residual, right_residual - 1, cur_res + ')')