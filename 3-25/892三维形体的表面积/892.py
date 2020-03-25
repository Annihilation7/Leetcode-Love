
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
            """
            不论每个格子有多少个正方体，必贡献 两底+(4*n)个侧面，n为正方体个数
            看下一个的时候，只需考虑侧面粘贴，减去就好了，
            侧面的面积计算公式 min(height1, height2)
            """
            res = 0

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] != 0:
                        level = grid[i][j]
                        res += (level * 4) + 2
                        # 看左侧和上侧
                        res -= min(grid[i][j], grid[i - 1][j]) * 2 if i >= 1 else 0
                        res -= min(grid[i][j], grid[i][j - 1]) * 2if j >= 1 else 0

            return res

