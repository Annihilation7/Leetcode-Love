#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 在两个排序数组中找到第k小的数.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/15 12:13 上午
#  Description : 比较难的二分搜索


class Solution:
    def getKthNum(self, alist1, alist2, k):
        m, n = len(alist1), len(alist2)
        assert 1 <= k <= m + n
        l = max(0, k - n)
        r = min(m, k)
        while l < r:
            mid = l + (r - l) // 2
            if alist2[k - mid - 1] > alist1[mid]:
                l = mid + 1
            else:
                r = mid
        list1_left_max = alist1[l - 1] if l > 0 else float('inf')
        list2_left_max = alist2[k - l - 1] if l != k else float('inf')
        return min(list1_left_max, list2_left_max)


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 4, 5]
    test = Solution()
    print(test.getKthNum(arr1, arr2, 9))
