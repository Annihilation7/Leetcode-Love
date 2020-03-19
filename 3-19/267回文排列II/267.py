

from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        res = []
        record = {}
        single_flag = 0

        # 统计
        for elem in s:
            record[elem] = record.get(elem, 0) + 1

        # 抓出出现次数为1次的字符
        single_char = ''
        for k, v in record.items():
            if v % 2 == 1:
                single_flag += 1
                record[k] -= 1
                single_char = k

        # 出现字符为1次的字符大于1，不满足条件，直接返回
        if single_flag > 1:
            return []

        # 取得呈pair的字符的一半，准备进行全排列
        chars = []
        for k, v in record.items():
            # 单个数目的字符不会进入循环体中
            for i in range(v // 2):
                chars.append(k)

        # 全排列这一半的元素
        permute = self.helper(chars)
        # 向结果中插入满足题意的全排列字符串
        for p in permute:
            res.append(p + single_char + p[::-1])
        return res

    def helper(self, chars):
        visited = [False] * len(chars)
        res = []

        def _helper(chars, idx, cur_char):
            nonlocal visited
            if idx == len(chars):
                res.append(''.join(cur_char))
                return
            for i in range(len(chars)):
                # 去重
                # 注意去重是 not visited[i - 1] !!!! 以前一直是 visited[i - 1]...
                if i > 0 and chars[i - 1] == chars[i] and not visited[i - 1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    cur_char.append(chars[i])
                    _helper(chars, idx + 1, cur_char)
                    cur_char.pop()
                    visited[i] = False

        _helper(chars, 0, [])
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.generatePalindromes("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))