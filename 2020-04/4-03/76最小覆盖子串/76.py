#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 76
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 1:02 上午
#  Description : 一道hastable + 滑动窗口


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        record_t = {}
        for elem in t:
            record_t[elem] = record_t.get(elem, 0) + 1

        res = s + '#'
        record_s = {}
        l = 0
        r = -1  # 左闭又闭，初始化时窗口内没有元素

        while l < len(s):
            if r + 1 < len(s):
                if not self._is_equal(record_s, record_t):
                    r += 1
                    record_s[s[r]] = record_s.get(s[r], 0) + 1
                else:
                    res = s[l: r + 1] if len(s[l: r + 1]) < len(res) else res
                    record_s[s[l]] -= 1  # 注意不是pop!而是计数-1
                    l += 1
            else:
                if not self._is_equal(record_s, record_t):
                    break  # r到头了，此时l继续往前不可能满足条件了，所以直接准备返回
                else:
                    res = s[l: r + 1] if len(s[l: r + 1]) < len(res) else res
                    record_s[s[l]] -= 1
                    l += 1

        return res if len(res) != len(s) + 1 else ""

    def _is_equal(self, record_s, record_t):
        for elem in record_t:
            if elem not in record_s or record_s[elem] < record_t[elem]:
                return False
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.minWindow("ADOBECODEBANC", "ABC"))


