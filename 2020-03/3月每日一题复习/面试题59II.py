#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 面试题59II.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/6 11:56 上午
#  Description : deque + queue


from collections import deque
import queue


class MaxQueue:

    def __init__(self):
        self.q = queue.Queue()
        self.max_q = deque()

    def max_value(self) -> int:
        if self.q.empty():
            return -1

        return self.max_q[0]

    def push_back(self, value: int) -> None:
        self.q.put(value)
        # 维护self.max_q
        while len(self.max_q) and value > self.max_q[-1]:
            self.max_q.pop()
        self.max_q.append(value)

    def pop_front(self) -> int:
        if self.q.empty():
            return -1

        ret = self.q.get()
        if ret == self.max_q[0]:  # 和最大值相等的时候也要维护max_q
            self.max_q.popleft()

        return ret



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()