#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 200
#  Author      : ZhenyuMa
#  Created     : 2020/4/2 9:11 下午
#  Description : dfs


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        self.m = len(grid)
        self.n = len(grid[0])
        self.d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.visited = [[False] * self.n for _ in range(self.m)]
        res = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1' and not self.visited[i][j]:
                    self.visited[i][j] = True
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, x, y):
        for _d in self.d:
            new_x = x + _d[0]
            new_y = y + _d[1]
            if self._check_valid(new_x, new_y) and grid[new_x][new_y] == '1' and not self.visited[new_x][new_y]:
                self.visited[new_x][new_y] = True
                self.dfs(grid, new_x, new_y)

    def _check_valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n


if __name__ == "__main__":
    test = Solution()
    print(test.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    ))
