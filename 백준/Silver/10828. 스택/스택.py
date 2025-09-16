import sys


class Stack:

    def __init__(self):
        self.lst = []
        self.point = 0

    def is_empty(self):
        if len(self.lst) == 0:
            return 1
        else:
            return 0


    def push(self, value):
        self.lst.append(value)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.lst.pop()

    def size(self):
        return len(self.lst)

    def top(self):
        if self.is_empty():
            return -1
        else:
            return self.lst[len(self.lst) - 1]



N = int(input())
stack = Stack()


for i in range(N):
    commend = list(sys.stdin.readline().split())
    if commend[0] == 'push':
        stack.push(int(commend[1]))
    elif commend[0] == 'top':
        print(stack.top())
    elif commend[0] == 'size':
        print(stack.size())
    elif commend[0] == 'pop':
        print(stack.pop())
    else:
        print(stack.is_empty())



