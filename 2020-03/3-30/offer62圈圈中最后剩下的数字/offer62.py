#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : offer62
#  Author      : ZhenyuMa
#  Created     : 2020/3/30 10:17 下午
#  Description : 暴力循环超时，这是一道约瑟夫环问题，利用反推法来求解


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        """反推法，最后一个数的安全位置肯定为0，且此时数组的容量为1"""
        res = 0
        for i in range(2, n + 1):  # 从两人开始反推
            res = (res + m) % i  # 上一次的索引 % 容量
        return res


if __name__ == "__main__":
    test = Solution()
    print(test.lastRemaining(5, 3))