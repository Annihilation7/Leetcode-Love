#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 93
#  Author      : ZhenyuMa
#  Created     : 2020/3/29 12:08 上午
#  Description : 暴力回溯


from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.helper(s, 0, '')
        return self.res

    def helper(self, s, dot_num, cur_res):
        if len(s) == 0:
            return

        if dot_num == 3:
            if len(s) == 1 or (len(s) > 1 and s[0] != '0' and int(s) <= 255):
                self.res.append(cur_res + s)
            return

        self.helper(s[1:], dot_num + 1, cur_res + s[0] + '.')
        if len(s) >= 2 and s[0] != '0':
            self.helper(s[2:], dot_num + 1, cur_res + s[:2] + '.')
        if len(s) >= 3 and s[0] != '0' and int(s[:3]) <= 255:
            self.helper(s[3:], dot_num + 1, cur_res + s[:3] + '.')