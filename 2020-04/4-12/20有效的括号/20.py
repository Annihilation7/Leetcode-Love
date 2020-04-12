#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 20.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/12 3:10 下午
#  Description : stack


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        record = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for elem in s:
            if elem in record:
                stack.append(elem)
            else:
                if len(stack) == 0 or record[stack[-1]] != elem:
                    return False
                stack.pop()

        return True if len(stack) == 0 else False