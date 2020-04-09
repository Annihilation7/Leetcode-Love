#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 3.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/9 9:07 下午
#  Description : 滑动窗口的题


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        record = {}
        l = 0
        r = -1

        while l < len(s):
            if r + 1 < len(s) and s[r + 1] not in record:
                r += 1
                record[s[r]] = r
            else:
                record.pop(s[l])  # 不满足条件会一直删的，没问题
                l += 1
            res = max(res, r - l + 1)

        return res