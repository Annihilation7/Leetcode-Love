#  -*- coding:utf-8 -*-

#  Editor      : Pycharm
#  File        : 953.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/19 下午11:54
#  Description :


from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.record = {s: i for i, s in enumerate(order)}
        return sorted(words, self._sort_key) == words

    def _sort_key(self, word1, word2):
        """其实就是写一个特殊的字典序比较函数"""
        if len(word1) != len(word2):
            if len(word1) <= len(word2):
                return -1
            else:
                return 1

        if word1 == word2:
            return -1

        for i in range(len(word1)):
            if self.record[word1[i]] < self.record[word2[i]]:
                return -1
            elif self.record[word1[i]] > self.record[word2[i]]:
                return 1


if __name__ == "__main__":
    s = "abc"
    d = "ab"
    x = sorted([s, d], key=lambda x, y: len(x) < len(y))