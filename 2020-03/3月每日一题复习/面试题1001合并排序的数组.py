#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 面试题 10.01. 合并排序的数组
#  Author      : ZhenyuMa
#  Created     : 2020/4/3 1:29 下午
#  Description : merge


from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i = m + n - 1
        j = m - 1
        k = n - 1

        while i >= 0:
            if j < 0:
                A[i] = B[k]
                k -= 1
            elif k < 0:
                A[i] = A[j]
                j -= 1
            elif A[j] >= B[k]:
                A[i] = A[j]
                j -= 1
            else:
                A[i] = B[k]
                k -= 1
            i -= 1