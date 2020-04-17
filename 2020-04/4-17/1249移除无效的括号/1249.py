#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 1249.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/17 11:51 下午
#  Description : 一看就是栈的题，无奈我太笨，看了提示才会


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalided = [False] * len(s)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                invalided[i] = True  # 先设为无效
                stack.append(i)  # 栈里存的是索引
            elif s[i] == ')':
                if len(stack) == 0:  # 没有匹配的左括号，那必然是无效的
                    invalided[i] = True
                else:  # 有匹配的，原先的那个(设为有效，并出栈
                    invalided[stack.pop()] = False

        res = ''
        for i in range(len(invalided)):
            if not invalided[i]:
                res += s[i]

        return res
