#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 994
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 2:21 下午
#  Description : bfs


from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        good_count = 0
        time = 0
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        while len(q):
            length = len(q)
            flag = False
            for i in range(length):
                x, y = q.popleft()
                for _d in d:
                    new_x = x + _d[0]
                    new_y = y + _d[1]
                    if self._check_valid(new_x, new_y, len(grid), len(grid[0])) \
                            and grid[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        good_count -= 1
                        flag = True
                        grid[new_x][new_y] = 2
            if not flag:
                break  # 本轮已经没有橘子被感染了，直接跳出循环，准备返回
            time += 1

        return time if good_count == 0 else -1

    def _check_valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n