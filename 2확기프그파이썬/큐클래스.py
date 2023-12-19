class Queue:
    def __init__(self): # 초기화 함수
        self.items = [] # 빈 리스트를 생성 

    def is_empty(self): # Queue가 비어 있는지 확인하는 함수
        return not bool(self.items)

    def enqueue(self, data): # Queue의 뒤쪽에 데이터를 추가하는 함수
        self.items.append(data)

    def dequeue(self): # Queue의 앞쪽에서 데이터를 가져오는 함수
        if self.is_empty(): # 만약 Queue가 비어 있다면
            print("Queue is empty.") # Queue가 비어 있다는 메시지를 출력 
            return None
        return self.items.pop(0) # Queue의 첫 번째 요소를 반환하고 삭제 

    def peek(self): # Queue의 앞쪽 데이터를 확인하는 함수
        if self.is_empty(): # 만약 Queue가 비어 있다면
            print("Queue is empty.") # Queue가 비어 있다는 메시지를 출력 
            return None
        return self.items[0] # Queue의 첫 번째 요소를 반환하되 삭제하지는 않는다.

queue = Queue() # Queue 인스턴스 생성

queue.enqueue(1) 
queue.enqueue(2) 
queue.enqueue(3) 

print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 