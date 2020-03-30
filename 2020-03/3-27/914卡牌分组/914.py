

from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """应该是一道hash table的题"""
        record = {}
        for elem in deck:
            record[elem] = record.get(elem, 0) + 1

        # 求全员个数的最大公约数
        x = None
        for k, v in record.items():
            if v == 1:
                return False
            # 就第一次执行，后面不会执行了
            if x is None:
                x = v
            x = self._gcd(x, v)
            if x == 1:  # x和v最大公约数为1，说明一定不能拆分成x个数组，每个数组中的值都相等这种情况
                return False
        return True

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)
