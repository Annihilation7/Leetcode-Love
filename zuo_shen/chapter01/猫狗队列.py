#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 猫狗队列
#  Author      : ZhenyuMa
#  Created     : 2020/3/31 10:25 下午
#  Description : 实现一个特殊的 猫狗队列


from collections import deque


# 猫A 狗B
class Pet:
    def __init__(self, type):
        self.type = type

    def getPetType(self):
        return self.type


class Cat(Pet):
    def __init__(self, type='cat'):
        super(Cat, self).__init__(type)


class Dog(Pet):
    def __init__(self, type='dog'):
        super(Dog, self).__init__(type)


# 不能改变上面的猫狗类，我们将猫、狗类进行封装，附带一个时间戳的功能
class PetWarpper:
    def __init__(self, type, count):
        self.data = Pet(type)
        self.count = count

    def getPet(self):
        return self.data

    def getCount(self):
        return self.count

    def getType(self):
        return self.data.type


class DogCatQueue:
    def __init__(self):
        """
        猫狗队列的实现，两个队列，一个放猫，一个放狗
        两个一起出队的时候看一下时间戳即可
        """
        self.dog_queue = deque()
        self.cat_queue = deque()
        self.count = 0  # 队列的时间戳，统一两个子队列

    def add(self, elem):
        self._check_elem_valid(elem)
        self.count += 1
        if elem == 'dog':
            self.dog_queue.append(PetWarpper(elem, self.count))
        else:
            self.cat_queue.append(PetWarpper(elem, self.count))

    def pollAll(self):
        if self.isEmpty():
            return None
        if len(self.dog_queue) == 0:
            return self.cat_queue.popleft().getPet().type
        elif len(self.cat_queue) == 0:
            return self.dog_queue.popleft().getPet().type
        else:
            # 两个队列都不为空，谁的时间戳小谁先出队列（先进先出）
            if self.dog_queue[0].getCount() > self.cat_queue[0].getCount():
                return self.cat_queue.popleft().getPet().type
            else:
                return self.dog_queue.popleft().getPet().type

    def pollDog(self):
        if len(self.dog_queue) == 0:
            return None
        return self.dog_queue.popleft().getPet().type

    def pollCat(self):
        if len(self.cat_queue) == 0:
            return None
        return self.cat_queue.popleft().getPet().type

    def isEmpty(self):
        return len(self.dog_queue) == 0 and len(self.cat_queue) == 0

    def _check_elem_valid(self, elem):
        assert elem in ['dog', 'cat'], 'invalid pet'


if __name__ == "__main__":
    q = DogCatQueue()
    elems = ['dog', 'dog', 'cat', 'dog', 'cat', 'dog']
    for elem in elems:
        q.add(elem)
    print(q.pollAll())
    print(q.pollCat())
    print(q.pollDog())

    print('-' * 40)
    while not q.isEmpty():
        print(q.pollAll())