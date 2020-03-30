

from collections import deque


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        """经典有向图BFS"""
        def op4(x, m, y, n):
            move = min(x, n - y)
            return (x - move, y + move)
        def op5(x, m, y, n):
            move = min(y, m - x)
            return (x + move, y - move)
        op = {
            0: lambda x, m, y, n: (m, y),  # 倒满A
            1: lambda x, m, y, n: (x, n),  # 倒满B
            2: lambda x, m, y, n: (0, y),  # 倒空A
            3: lambda x, m, y, n: (x, 0),  # 倒空B
            4: lambda x, m, y, n: op4(x, m, y, n),  # A倒入B，倒满或者A空
            5: lambda x, m, y, n: op5(x, m, y, n)  # B倒入A，倒满或者B空
        }

        record = set()
        q = deque()
        q.append((0, 0))
        record.add((0, 0))

        while len(q):
            pop_x, pop_y = q.popleft()
            if pop_x + pop_y == z:
                return True
            for i in range(6):
                next_state = op[i](pop_x, x, pop_y, y)
                if next_state not in record:
                    record.add(next_state)
                    q.append(next_state)

        return False


if __name__ == '__main__':
    test = Solution()
    print(test.canMeasureWater(3, 5, 4))
