#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : main.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/8 11:21 下午
#  Description : dfs


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.visited = [[False] * n for _ in range(m)]
        return self._dfs(0, 0, m, n, k)

    def _dfs(self, i, j, m, n, k):
        if not self._check_valid(i, j, m, n) or \
                self.visited[i][j] or \
                self._cal_num(i) + self._cal_num(j) > k:
            return 0

        self.visited[i][j] = True
        return 1 + self._dfs(i - 1, j, m, n, k) + self._dfs(i, j + 1, m, n, k) \
               + self._dfs(i + 1, j, m, n, k) + self._dfs(i, j - 1, m, n, k)

    def _check_valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n

    def _cal_num(self, num):
        res = 0
        while num:
            res += num % 10
            num //= 10
        return res


if __name__ == "__main__":
    test = Solution()
    print(test.movingCount(1, 2, 1))