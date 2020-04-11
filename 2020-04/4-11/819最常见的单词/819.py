#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 819.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/12 12:26 上午
#  Description :


from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[!?\',;.]', ' ', paragraph)
        banned = set(banned)
        record = {}

        max_count = 0
        ret = None
        for p in paragraph.split():
            p = p.lower()
            if p not in banned:
                record[p] = record.get(p, 0) + 1
                if record[p] > max_count:
                    max_count = record[p]
                    ret = p

        return ret