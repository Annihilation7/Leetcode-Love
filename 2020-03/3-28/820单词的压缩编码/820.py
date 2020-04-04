#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 820
#  Author      : ZhenyuMa
#  Created     : 2020/3/28 11:03 下午
#  Description : 一道前缀树的题


from typing import List


class Node:
    def __init__(self, isWord=False):
        self.isWord = isWord
        self.next = {}


class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0

    def add(self, astring):
        cur_node = self.root
        for elem in astring:
            if cur_node.next.get(elem, None) is None:
                cur_node.next[elem] = Node()
            cur_node = cur_node.next[elem]
        if not cur_node.isWord:
            cur_node.isWord = True
            self.size += 1

    def is_prefix(self, astring):
        """前缀不用判断isword是否匹配"""
        cur_node = self.root
        for elem in astring:
            if cur_node.next.get(elem, None) is None:
                return False
            cur_node = cur_node.next[elem]
        return True


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        aux = Trie()
        res = 0
        # 按长度先反排一下
        # 因为是前缀树，而这道题显然是一个后缀的概念，所以我们反插入字符串
        words = sorted([word[::-1] for word in words], key=lambda x: -len(x))

        for word in words:
            if not aux.is_prefix(word):
                aux.add(word)
                res += len(word) + 1

        return res

