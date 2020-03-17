

from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """计算IOU的题，23333"""
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2

        min_maxx = min(x12, x22)
        max_minx = max(x11, x21)
        min_maxy = min(y12, y22)
        max_miny = max(y11, y21)

        return (min_maxx - max_minx) > 0 and  (min_maxy - max_miny) > 0