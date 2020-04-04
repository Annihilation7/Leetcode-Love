#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 1162
#  Author      : ZhenyuMa
#  Created     : 2020/3/29 11:43 下午
#  Description : bfs


from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = [[False] * n for _ in range(m)]
        res = None

        q = deque()
        is_valid = False

        # 装陆地
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))  # 0代表初始距离
                    visited[i][j] = True

        while len(q):
            x, y, dis = q.popleft()
            for _d in d:
                new_x = x + _d[0]
                new_y = y + _d[1]
                if self._check_valid(new_x, new_y, m, n) and not visited[new_x][new_y]:
                    is_valid = True
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y, dis + 1))
                    res = dis + 1

        if not is_valid:
            return -1

        return res

    def _check_valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
