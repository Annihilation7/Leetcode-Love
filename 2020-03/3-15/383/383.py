

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """一道hash table的题"""
        record = {}
        # 先记录一个magazine
        for elem in magazine:
            record[elem] = record.get(elem, 0) + 1

        # 遍历ransomNote
        for elem in ransomNote:
            # 不包含字符
            if elem not in record:
                return False
            record[elem] -= 1
            # 字符数目不够
            if record[elem] < 0:
                return False

        return True