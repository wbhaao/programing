class Deque:
    def __init__(self):
        self.rear = 0
        self.front = 0
        self.MAX_SIZE = 100
        self.deq = [0 for i in range(self.MAX_SIZE)]

    def get_rear(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return -1
        return self.deq[self.rear-1]  
  
    def is_empty(self):
        return self.rear == self.front  
 
    def is_full(self):
        return (self.rear+1)%self.MAX_SIZE == self.front  

    def add_rear(self, x):
        if self.is_full():
            print("ERROR: FULL")
            return
        self.deq[self.rear] = x
        self.rear = (self.rear+1)%self.MAX_SIZE  

    def add_front(self, x):
        if self.is_full():
            print("ERROR: FULL")
            return
        self.front = (self.front - 1 + self.MAX_SIZE) % self.MAX_SIZE
        self.deq[self.front] = x  
    
    def del_front(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return
        self.front = (self.front +1) % self.MAX_SIZE
        return self.deq[self.front-1]  
    
    def del_rear(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return
        self.rear = (self.rear - 1 + self.MAX_SIZE) % self.MAX_SIZE
        return self.deq[self.rear]  
