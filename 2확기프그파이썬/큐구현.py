class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = self.rear = 0

    def is_empty(self):
        return self.queue[self.front] is None

    def is_full(self):
        return self.queue[self.rear] is not None

    def enqueue(self, value):
        if self.is_full():
            print('큐가 가득 찼습니다.')
            return
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.display_queue()

    def dequeue(self):
        if self.is_empty():
            print('큐가 비었습니다.')
            return
        dequeued_value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.display_queue()
        return dequeued_value

    def display_queue(self):
        print('큐 상태:', self.queue)


queue = CircularQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # 큐가 가득 찼다는 메시지가 출력되어야 합니다.

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  # 큐가 비었다는 메시지가 출력되어야 합니다.

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
