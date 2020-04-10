#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 415.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/10 11:19 下午
#  Description : 和那个链表相加的思路是一样的


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        length_offset = len(num2) - len(num1)
        new_num1 = '0' * length_offset + num1
        assert len(new_num1) == len(num2)

        c = 0
        res = ''
        for i in range(len(num2) - 1, -1, -1):
            _sum = int(new_num1[i]) + int(num2[i]) + c
            true_sum = _sum % 10
            c = _sum // 10
            res = str(true_sum) + res
        if c == 1:
            res = '1' + res
        return res