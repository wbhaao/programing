QUEUE_SIZE = 5

class CircularQueue:
    def __init__(self, capacity=QUEUE_SIZE):
        self.capacity = capacity
        self.list = [None]*capacity
        self.front = 0
        self.rear = 0
    def isEmpty(self):
        return not bool(self.list[self.front])
    def isFull(self):
        return bool(self.list[self.rear])
    def enqueue(self, value) :
        if self.isFull():
            print('채워졌어용')
            return
        self.list[self.rear] = value
        self.rear = (self.rear + 1)%QUEUE_SIZE

        self.peak(self.list[self.rear])
    def dequeue(self):
        if self.isEmpty():
            print('비엇어용')
            return
        ans = self.list[self.front]
        self.list[self.front] = None
        self.front = (self.front + 1)%QUEUE_SIZE

        self.peak(ans)
    def peak(self, value):
        print('얘를 수정함',value, self.list)
queue = CircularQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(3)
queue.enqueue(3)