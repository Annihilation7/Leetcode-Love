#  -*- coding:utf-8 -*-

#  Editor      : Pycharm
#  File        : 49.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/18 下午11:06
#  Description : hash table的题


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = defaultdict(list)

        for elem in strs:
            record[tuple(sorted(elem))].append(elem)  # 异位词排序后肯定是相同的
            # 转tuple变成可哈希的对象即可，就能进行记录操作了

        return list(record.values())
