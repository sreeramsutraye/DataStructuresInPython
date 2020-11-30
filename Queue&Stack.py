class Queue:
    def __init__(self,que):
        self.que = que
    def enque(self,data):
        self.que.append(data)
    def enqueMultipleItems(self,*data):
        for d in data:
            self.que.append(d)
    def deque(self):
        for i in range(1,len(que)):
            self.que[i-1] = self.que[i]
        self.que.pop()
    def printQue(self):
        print(end=" | ")
        for i in self.que:
            print(i,end=" | ")
        print()
class Stack:
    def __init__(self,stack):
        self.stack = stack
    def push(self,data):
        self.stack.append(data)
    def pushMultipleItems(self,*data):
        for d in data:
            self.stack.append(d)
    def pop(self):
        self.stack.pop()
    def printStack(self):
        print(end=" | ")
        for i in self.stack:
            print(i,end=" | ")
        print()
que = []
q = Queue(que)
q.enque(0)
q.enqueMultipleItems(1,9,4,8,4,6,2,85,4)
q.deque()
q.printQue()
sck = []
stack = Stack(sck)
stack.push(1)
stack.pushMultipleItems(4,7,9,46,8,4,89,4,7)
stack.pop()
stack.printStack()
