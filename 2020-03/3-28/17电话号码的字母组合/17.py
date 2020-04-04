#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 17
#  Author      : ZhenyuMa
#  Created     : 2020/3/28 11:44 下午
#  Description : 回溯


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        self.record = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8字符串转换整数': 'tuv',
            '9': 'wxyz'
        }
        self.res = []
        self.helper(digits, 0, '')
        return self.res

    def helper(self, digits, idx, cur_digit):
        if idx == len(digits):
            self.res.append(cur_digit)
            return

        for digit in self.record[digits[idx]]:
            self.helper(digits, idx + 1, cur_digit + digit)