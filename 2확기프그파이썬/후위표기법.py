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
    def peek(self):
        return self.stack[0]
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

def precedence(op): # 연산자의 우선순위를 결정하는 함수
    if op == '(' or op == ')': # 괄호가 가장 낮은 우선순위를 가짐
        return 0
    elif op == '+' or op == '-': # 덧셈과 뺄셈이 그 다음으로 우선순위
        return 1
    elif op == '*' or op == '/': # 곱셈과 나눗셈이 가장 높은 우선순위를 가짐
        return 2
    else: # 기타 문자는 -1을 반환
        return -1

def Infix2Postfix(expr): # 중위 표현식을 후위 표현식으로 변환하는 함수
    s = Stack() # 초기화
    output = [] # output 초기화

    for term in expr: # 표현식의 각 요소에 대해 반복
        if term in '(': # 요소가 "(" 이라면
            s.push('(') # 스택 "(" 바로 푸시
        elif term in ')': # 요소가 ")" 이라면
            while not s.isEmpty(): # 스택이 비어있지 않은 동안
                op = s.pop() # 스택의 맨 위 요소를 팝
                if op == '(': # 팝한 요소가 "(" 이라면
                    break # 반복문을 빠져나옴
                else: # 아니라면
                    output.append(op) # 삭제 요소 output에 추가
        elif term in "+-*/": # 요소가 연산자라면
            while not s.isEmpty(): # 스택이 비어있지 않은 동안
                op = s.peek() # 스택의 맨 위 요소를 확인
                if (precedence(term) <= precedence(op)): # 현재 요소의 우선순위가 스택 맨 위 요소의 우선순위보다 낮거나 같다면
                    output.append(op) # 스택의 맨 위 요소를 팝하여 output에 추가
                    s.pop()
                else: # 아니라면
                    break # 반복문을 빠져나옴
            s.push(term) # 현재 요소를 스택에 푸시
        else: # 요소가 숫자라면
            output.append(term) # output에 추가

    while not s.isEmpty(): # 스택이 비어있지 않다면
        output.append(s.pop()) # 스택의 모든 요소를 팝하여 output에 추가

    return output # output을 반환

print(Infix2Postfix("1*2/3*(2+1)")) # "1*2/3*(2+1)" 의 중위 표현식을 후위 표현식으로 변환하여 출력
