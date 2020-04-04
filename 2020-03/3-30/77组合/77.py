#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 77
#  Author      : ZhenyuMa
#  Created     : 2020/3/30 11:19 下午
#  Description : 组合问题，也是回溯整


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """无重复元素"""
        self.res = []
        self.visited = [False] * (n + 1)
        self.helper(n, k, 1, [])
        return self.res

    def helper(self, n, m, idx, cur_res):
        if len(cur_res) == m:
            self.res.append(cur_res[:])
            return

        for i in range(idx, n - m):
            if not self.visited[i]:
                cur_res.append(i)
                self.visited[i] = True
                self.helper(n, m, i + 1, cur_res)
                cur_res.pop()
                self.visited[i] = False
