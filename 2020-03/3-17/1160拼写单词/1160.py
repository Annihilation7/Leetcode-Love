

from typing import List
import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """我所想到的就是hash table + 遍历。。。"""
        res = 0
        record_chars = collections.Counter(chars)

        for word in words:
            record_word = collections.Counter(word)
            if all(record_word[w] <= record_chars[w] for w in word):
                res += len(word)

        return res


if __name__ == '__main__':
    test = 'asdwdwasd'
    counter = collections.Counter(test)
    print(counter)
    print(counter['meiyouzhege'])  # 默认是0！所以可以看成是 defaultdict(int)

