#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : main.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/12 11:45 上午
#  Description : 就是初中几何知识，只不过要考虑斜率为无穷大的直线


from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int],
                     start2: List[int], end2: List[int]) -> List[float]:
        x1_1, y1_1 = start1
        x1_2, y1_2 = end1
        x2_1, y2_1 = start2
        x2_2, y2_2 = end2

        k1 = (y1_2 - y1_1) / (x1_2 - x1_1) if x1_1 != x1_2 else None
        b1 = y1_1 - k1 * x1_1 if k1 is not None else None
        k2 = (y2_2 - y2_1) / (x2_2 - x2_1) if x2_1 != x2_2 else None
        b2 = y2_1 - k2 * x2_1 if k2 is not None else None

        # 两条都是垂直线
        if k1 is None and k2 is None:
            if x1_1 == x2_1 and \
                    min(y1_1, y1_2) <= max(y2_1, y2_2) \
                    and min(y2_1, y2_2) <= max(y1_1, y1_2):
                return [x1_1, max(min(y1_1, y1_2), min(y2_1, y2_2))]
        # 有一条是垂线
        elif k1 is None:
            y = k2 * x1_1 + b2
            if (y1_1 - y) * (y1_2 - y) <= 0:
                return [x1_1, y]
        elif k2 is None:
            y = k1 * x2_1 + b2
            if (y1_1 - y) * (y1_2 - y) <= 0:
                return [x2_1, y]
        # 两条都是正常的线
        else:
            # 部分重合
            if k1 == k2 and b1 == b2 and \
                    min(y1_1, y1_2) <= max(y2_1, y2_2) and \
                    min(y2_1, y2_2) <= max(y1_1, y1_2):
                return [max(min(x1_1, x1_2), min(x2_1, x2_2)),
                        max(min(y1_1, y1_2), min(y2_1, y2_2))]
            elif k1 != k2:
                x = (b2 - b1) / (k1 - k2)
                y = k1 * x + b1
                if (y1_2 - y) * (y1_1 - y) <= 0 and (y2_1 - y) * (
                        y2_2 - y) <= 0:
                    return [x, y]

        return []


if __name__ == "__main__":
    test = Solution()
    # 两条都是垂线
    print(test.intersection([1, 1], [-1, 1], [1, 0], [-3, 2]))
