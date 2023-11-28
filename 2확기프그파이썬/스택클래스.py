class Stack():
    def __init__(self):
        # 스택 초기화
        self.stack = []  

    def push(self, data):
        # 스택 상단에 데이터 추가
        self.stack.append(data)  

    def pop(self):
        pop_object = None
        if self.isEmpty():
            # 스택 비어있으면 메시지 출력
            print("Stack is Empty")  
        else:
            # 상단 데이터 제거하고 반환
            pop_object = self.stack.pop()  
            
        return pop_object
            
    def top(self):
        top_object = None
        if self.isEmpty():
            # 스택 비어있으면 메시지 출력
            print("Stack is Empty")  
        else:
            # 스택 비어있지 않으면 맨 상단데이터 반환
            top_object = self.stack[-1]  
            
        return top_object
            
    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            # 스택이 비어있으면 True 반환
            is_empty = True  
        return is_empty
    
    def deleteOne(self, data):
        # 임시스택 생성
        stack_temp = Stack()  
        # 원래 스택의 요소들을 역순으로 검사
        for s in reversed(self.stack):  
            # 해당 데이터를 찾았다면
            if s == data:  
                # 원래 스택에서 데이터 제거
                self.stack.pop()  
                # 임시스택이 빌때까지
                while stack_temp.stack:  
                    # 임시스택의 요소들을 원래 스택으로 이동
                    self.stack.append(stack_temp.pop())  
                # 데이터 삭제완료
                return True  
            else:
                # 해당 데이터가 아니라면 임시 스택으로 이동 (임시스택으로 stack 복원)
                stack_temp.push(self.stack.pop())  
        # 해당 데이터를 찾지 못했다면 False 반환
        return False  

    def clear(self):
        # 스택이 비어있다면 함수종료
        if self.isEmpty():
            return  
        while not self.isEmpty():
            # 스택이 비어있지 않다면 모든 요소 제거
            self.pop()  
        # 스택의 모든 요소 제거 완료
        return True  
    
    def reverse_print(self):
        if self.isEmpty():
            # 스택이 비어있다면 메시지 출력
            print("Stack is Empty")  
            return None
        else:
            # 임시 스택 생성
            stack_temp = Stack()  
            while not self.isEmpty():
                # 원래 스택의 요소들을 임시 스택으로 이동
                stack_temp.push(self.pop())  
            for i in stack_temp.stack:
                # 임시 스택의 요소들을 출력
                print(i, end=' ')  
            while not stack_temp.isEmpty():
                # 임시 스택의 요소들을 원래 스택으로 이동
                self.push(stack_temp.pop())  

s = Stack()  
s.push(1)  
s.push(2)  
s.push(3)  
print(s.stack)  
s.deleteOne(2)  
print(s.stack)  
s.reverse_print()  