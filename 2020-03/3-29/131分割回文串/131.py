#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 131分割回文串
#  Author      : ZhenyuMa
#  Created     : 2020/3/29 11:47 下午
#  Description : 回溯


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.helper(s, [])
        return self.res

    def helper(self, s, cur_res):
        if len(s) == 0:
            self.res.append(cur_res[:])
            return

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                cur_res.append(s[:i])
                self.helper(s[i:], cur_res)
                cur_res.pop()


if __name__ == '__main__':
    test = Solution()
    print(test.partition('aab'))