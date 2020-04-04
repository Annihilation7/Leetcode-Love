#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 225
#  Author      : ZhenyuMa
#  Created     : 2020/4/3 1:04 下午
#  Description : 双队列实现栈


from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self.size = 0


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self.size += 1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self._aux()
        ret = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        self.size -= 1
        return ret


    def top(self) -> int:
        """
        Get the top element.
        """
        self._aux()
        ret = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return ret


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0

    def _aux(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

