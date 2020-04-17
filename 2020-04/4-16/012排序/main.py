#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : main.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/16 9:43 下午
#  Description : 三路partition的思路


class Solution:
    def func(self, alist):
        l = -1
        r = len(alist)
        i = 0

        while i < r:
            if alist[i] == 1:
                i += 1
            elif alist[i] < 1:
                l += 1
                self._swap(alist, i, l)
                i += 1
            else:
                r -= 1
                self._swap(alist, i, r)

        return alist

    def _swap(self, alist, i, j):
        alist[i], alist[j] = alist[j], alist[i]


if __name__ == "__main__":
    test = Solution()
    print(test.func([2, 1, 1, 0, 2, 2, 1, 1, 1, 2, 1, 2, 0, 0]))