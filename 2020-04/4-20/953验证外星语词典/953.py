#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 953.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/20 11:41 下午
#  Description : 相当于写一个排序的lambda函数


from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.record = {k: i for i, k in enumerate(order)}
        # 验证有序就是遍历一次看相邻即可，要比4月19号那天的思好很多
        for i in range(1, len(words)):
            if not self._cmp(words[i - 1], words[i]):
                return False
        return True

    def _cmp(self, word1, word2):
        max_length = max(len(word1), len(word2))
        for i in range(max_length):
            if i == len(word1):
                return True
            elif i == len(word2):
                return False
            else:
                if self.record[word1[i]] < self.record[word2[i]]:
                    return True
                else:
                    return False


if __name__ == "__main__":
    test = Solution()
    print(test.isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz"))