class Queue:
    def __init__(self, n):
        self.front = self.rear = -1
        self.Q = [0] * n

    def enQueue(self, item):
        global rear
        if self.isFull(): print("Queue_Full")
        else:
            self.rear +=1
            self.Q[self.rear] = item

    def deQueue(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            self.front += 1
            return self.Q[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == len(self.Q) -1

    # 제일 앞에 있는거 반환만 함.
    def Qpeek(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            return self.Q[self.front+1]


# 앞으로 밀착
class Queue2:
    def __init__(self, n):
        self.front = 0
        self.rear = -1
        self.Q = [0] * n

    def enQueue(self, item):
        global rear
        if self.isFull(): print("Queue_Full")
        else:
            self.rear +=1
            self.Q[self.rear] = item

    def deQueue(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            self.rear -= 1
            tmp = self.Q[0]
            for i in range(self.rear+1):
                self.Q[i] = self.Q[i+1]
            self.Q[self.rear+1] = tmp

            return self.Q[self.rear+1]

    def isEmpty(self):
        return self.front == self.rear+1

    def isFull(self):
        return self.rear == len(self.Q) -1

    # 제일 앞에 있는거 반환만 함.
    def Qpeek(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            return self.Q[self.front+1]

my_Queue = Queue2(10)
my_Queue.enQueue(1)
my_Queue.enQueue(2)
my_Queue.enQueue(3)
print(my_Queue.deQueue())
print(my_Queue.deQueue())
print(my_Queue.deQueue())