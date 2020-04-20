#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 200.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/20 11:38 下午
#  Description : dfs


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        self.m = len(grid)
        self.n = len(grid[0])
        self.d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        res = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        for _d in self.d:
            new_i = i + _d[0]
            new_j = j + _d[1]
            if self.check_valid(new_i, new_j) and grid[new_i][new_j] == '1':
                self.dfs(grid, new_i, new_j)

    def check_valid(self, i, j):
        return 0 <= i < self.m and 0 <= j < self.n