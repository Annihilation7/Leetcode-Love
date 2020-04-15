#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 542.py
#  Author      : ZhenyuMa
#  Created     : 2020-04-15 21:51
#  Description : bfs


from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        distance_map = matrix.copy()
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        q = deque()
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visited[i][j] = True
                    q.append((i, j, 0))

        while len(q):
            pop_x, pop_y, dis = q.popleft()
            for _d in d:
                new_x = pop_x + _d[0]
                new_y = pop_y + _d[1]
                if self._check_valid(new_x, new_y, m, n) and not visited[new_x][new_y]:
                    distance_map[new_x][new_y] = dis + 1
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y, dis + 1))

        return distance_map

    def _check_valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
