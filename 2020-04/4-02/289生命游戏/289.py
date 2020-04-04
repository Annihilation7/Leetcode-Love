#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 289
#  Author      : ZhenyuMa
#  Created     : 2020/4/2 8字符串转换整数:51 下午
#  Description : 遍历即可，但是有一个利用二进制编码信息的优化过程


from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        四种状态：
            00 : 当前死，下一轮还是死
            01 ：当前活，下一轮死
            10 : 当前死，下一轮活
            11 : 当前活，下一轮活
        """
        self.d = [
            [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]
        ]
        self.m = len(board)
        self.n = len(board[0])

        for x in range(self.m):
            for y in range(self.n):
                one_count = self.get_count(board, x, y)
                # 只管活的，因为后面右移的时候就自动维护没考虑的坐标了，直接置成了0
                if board[x][y] == 1 and (one_count == 2 or one_count == 3):
                    board[x][y] = 3  # 继续活
                elif board[x][y] == 0 and one_count == 3:
                    board[x][y] = 2  # 当前死，下一轮活

        # 正式更新board
        for x in range(self.m):
            for y in range(self.n):
                board[x][y] >>= 1

    def get_count(self, board, x, y):
        count = 0
        for _d in self.d:
            new_x = x + _d[0]
            new_y = y + _d[1]
            if self._check_valid(new_x, new_y):
                count += (board[new_x][new_y] & 1)  # 考虑当前状态是活的即可
        return count

    def _check_valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n
