#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : main.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/16 9:38 下午
#  Description : 字符串转整型


class Solution:
    def func(self, astring):
        res = 0

        for i in range(len(astring)):
            res = (res * 10) + (ord(astring[i]) - ord('0'))

        return res


if __name__ == '__main__':
    test = Solution()
    print(test.func('123456789'))