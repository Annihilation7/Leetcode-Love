#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 用一个栈实现另一个栈的排序
#  Author      : ZhenyuMa
#  Created     : 2020/4/1 10:33 下午
#  Description : 两个栈来回折腾元素，类似单调栈


class Solution:
    def sortStackByStack(self, stack):
        """注意排序的是该栈本身，不能返回新栈，所以逻辑变成从小到大，然后倒回原栈即可"""
        aux_stack = []

        while len(stack):
            pop_elem = stack.pop()
            while len(aux_stack) and pop_elem > aux_stack[-1]:
                stack.append(aux_stack.pop())
            aux_stack.append(pop_elem)

        # 倒回原栈
        while len(aux_stack):
            stack.append(aux_stack.pop())

        return stack


if __name__ == "__main__":
    test = Solution()
    print(test.sortStackByStack([5, 4, 3, 2, 1]))