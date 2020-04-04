#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 1111
#  Author      : ZhenyuMa
#  Created     : 2020/4/1 8字符串转换整数:11 下午
#  Description : 一道栈的题


from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        每次入栈一个左括号，栈深度闭加一。题目的意思是尽可能让两个栈的深度平衡。
        才能得到max(stack_depth1, stack_depth2)最小
        那么偶数深度赋0，基数深度赋1，是比较好的选择
        """
        res = [-1] * (len(seq))
        depth = 0

        for i, elem in enumerate(seq):
            if elem == '(':
                depth += 1
                res[i] = depth % 2
            else:
                # 这回要先取模，因为')'是有和它匹配的')'的，他俩深度是一样的，所以先取模，然后再维护depth
                res[i] = depth % 2
                depth -= 1

        return res


if __name__ == "__main__":
    test = Solution()
    print(test.maxDepthAfterSplit("()(())()"))