

from typing import List
from collections import deque

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """
        就是一道bfs的题。也可以用桶排序来做。时间复杂度是O(R*C)
        注意曼哈顿距离的定义，还有visited的定义，防止重复选取元素
        """
        res = []
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = [False] * (R * C)
        q = deque()
        q.append((r0, c0))
        res.append([r0, c0])
        visited[r0 * C + c0] = True

        while len(q):
            pop_x, pop_y = q.popleft()
            for _d in d:
                new_x = pop_x + _d[0]
                new_y = pop_y + _d[1]
                visited_idx = new_x * C + new_y
                if self._check_valid(new_x, new_y, R, C) and \
                        not visited[visited_idx]:
                    res.append([new_x, new_y])
                    q.append((new_x, new_y))
                    visited[visited_idx] = True

        return res

    def _check_valid(self, i, j, R, C):
        return 0 <= i < R and 0 <= j < C


if __name__ == '__main__':
    test = Solution()
    test_case = [2, 3, 1, 2]
    print(test.allCellsDistOrder(*test_case))