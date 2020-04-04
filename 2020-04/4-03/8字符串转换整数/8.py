#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 8
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 12:54 上午
#  Description : python不一行完成对不起自己


import re


class Solution:
    def myAtoi(self, str: str) -> int:
        # *用的很精髓，用到了 int(*([])) = 0 的特性
        return min(max(int(*(re.findall('^[\+\-]?\d+', str.strip()))), -2 ** 31), 2 ** 31 - 1)