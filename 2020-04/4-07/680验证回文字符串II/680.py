#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 680.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/10 11:36 下午
#  Description : 双指针 一个容错1


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        return self.helper(s, 0, len(s) - 1, False)

    def helper(self, s, l, r, remove_flag):
        if l >= r:
            return True

        if s[l] == s[r]:
            return self.helper(s, l + 1, r - 1, remove_flag)
        else:
            if not remove_flag:
                return self.helper(s, l + 1, r, True) or self.helper(s, l, r - 1, True)

        return False