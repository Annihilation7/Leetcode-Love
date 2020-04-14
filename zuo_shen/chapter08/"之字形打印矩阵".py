#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : "之字形打印矩阵".py
#  Author      : ZhenyuMa
#  Created     : 2020/4/14 11:39 下午
#  Description : 挺有意思的一道题


class Solution:
    def printMatrixZigZag(self, matrix):
        m, n = len(matrix), len(matrix[0])
        x1, y1, x2, y2 = 0, 0, 0, 0
        down2up = True
        res = []
        while not (x1 == m - 1 and x2 == m - 1):
            res.extend(self._print_diagonal(matrix, x1, y1, x2, y2, down2up))
            if x1 == m - 1:
                y1 += 1
            else:
                x1 += 1

            if y2 == n - 1:
                x2 += 1
            else:
                y2 += 1
            down2up = not down2up
        res.append(matrix[-1][-1])
        return res

    def _print_diagonal(self, matrix, x1, y1, x2, y2, down2up):
        res = []
        if down2up:
            while x1 >= x2:
                res.append(matrix[x1][y1])
                x1 -= 1
                y1 += 1
        else:
            while x2 <= x1:
                res.append(matrix[x2][y2])
                x2 += 1
                y2 -= 1
        return res


if __name__ == "__main__":
    test = Solution()
    print(test.printMatrixZigZag([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]))
