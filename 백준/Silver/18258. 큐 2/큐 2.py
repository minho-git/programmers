import sys

class Queue:
    def __init__(self, capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * self.capacity

    def is_empty(self):
        if self.no == 0:
            return 1
        else:
            return 0

    def size(self):
        return self.no

    def start(self):
        if self.is_empty():
            return -1
        else:
            return self.que[self.front]

    def back(self):
        if self.is_empty():
            return -1
        else:
            return self.que[self.rear - 1 if self.rear != 0 else self.capacity - 1]

    def enqueue(self, value):
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1

        if self.rear >= self.capacity:
            self.rear = 0

    def dequeue(self):
        if self.is_empty():
            return -1
        else:
            x = self.que[self.front]
            self.front += 1
            self.no -= 1

            if self.front == self.capacity:
                self.front = 0

            return x


N = int(input())
queue = Queue(2000000)


for i in range(N):
    commend = list(sys.stdin.readline().split())
    if commend[0] == 'push':
        queue.enqueue(commend[1])
    elif commend[0] == 'pop':
        print(queue.dequeue())
    elif commend[0] == 'empty':
        print(queue.is_empty())
    elif commend[0] == 'size':
        print(queue.size())
    elif commend[0] == 'front':
        print(queue.start())
    else:
        print(queue.back())