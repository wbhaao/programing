# stack
class Stack():
    def __init__(self):
        self.top = -1;
        self.stack = [0] * 5
        self.max_size = 5

    def isEmpty(self):
        return self.top==-1
    
    def isFull(self):
        return self.top==self.max_size-1
    
    def push(self, item):
        if self.isFull():
            print("꽉찼어요")
            return
        self.top += 1
        self.stack[self.top] = item
    
    def pop(self):
        if self.isEmpty():
            print("비었어요")
            return
        deleted = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -= 1
        return deleted
    
s = Stack()
s.push(1)
print(s.stack)
s.push(2)
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)

# queue
class Queue():
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.queue = [0] * 5
        self.max_size = 5
    
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.rear == self.max_size-1
    
    def enqueue(self, item):
        if self.isFull():
            print("꽉")
            return 
        self.rear += 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("텅")
            return
        deleted = self.queue[self.front]
        self.front += 1
        self.queue[self.front] = 0
        return deleted
print("QUEUEUEUE")
q = Queue()
print(q.queue)
q.enqueue(1)
print(q.queue)
q.enqueue(2)
print(q.queue)
q.enqueue(3)
print(q.queue)


q.dequeue()
print(q.queue)
q.dequeue()
print(q.queue)
q.dequeue()
print(q.queue)

# 원형 큐
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.max_size = 5
        self.items = [None] * 5

    def isEmpty(self):
        return self.front == self.rear 
    
    def isFull(self):
        return self.front == (self.rear+1)%self.max_size
    
    def enqueue(self, item):
        if self.isFull():
            print("꽉")
            return 
        self.rear = (self.rear+1)%self.max_size
        self.items[self.rear] = item

    # 삭제하지 않는 이유 : 삭제 안해도 어차피 안보임
    def dequeue(self):
        if self.isEmpty():
            print("텅")
            return
        self.front = (self.front+1)%self.max_size
        return self.items[self.front]
    
print("\n\nCQ\n\n")
q = CircularQueue()
q.enqueue(1)
print(q.front, q.rear, q.items)
q.enqueue(2)
print(q.front, q.rear, q.items)
q.enqueue(3)
print(q.front, q.rear, q.items)
q.enqueue(4)
print(q.front, q.rear, q.items)
q.enqueue(5)
print(q.front, q.rear, q.items)
q.enqueue(6)
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)
q.enqueue(4)
print(q.front, q.rear, q.items)
q.enqueue(5)
print(q.front, q.rear, q.items)
q.enqueue(6)
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)
print("deleted", q.dequeue())
print(q.front, q.rear, q.items)

# 데크
class Deque():
    def __init__(self):
        self.front = -1
        self.rear = -1

print("\n\nDeque\n\n")
q = CircularQueue()

