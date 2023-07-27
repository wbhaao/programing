
'''

a = input()
i = 0
lst = []
def plusI():
    global i
    if i+1>=len(a):
        if lst != []:
            print(''.join(map(str, reversed(lst))), end="")
        exit()
    else:
        i += 1
while i < len(a):
    if a[i]=='<':
        if lst!=[]:
            print(''.join(map(str, reversed(lst))), end="")
            lst = []  
        while a[i]!='>':
            lst.append(a[i])
            plusI()
        lst.append(a[i])
        print(''.join(map(str, lst)), end="")
        lst = []    
        plusI()
        continue
    if a[i] == ' ':
        print(''.join(map(str, reversed(lst))), end=" ")
        lst = []    
        plusI()
        continue
    lst.append(a[i])
    plusI()
if lst != []:
    print(''.join(map(str, reversed(lst))), end="")
    
'''    
## 빠른 풀이, 내꺼랑 비슷한데 더 빠름
import sys
word = list(sys.stdin.readline().rstrip())
i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += word[i:].index(">")+1   # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다
print("".join(word))
'''
## 모범 답안, 근데 엄청 느림
import sys
S = sys.stdin.readline().strip() + ' ' # 마지막에 공백을 더해주자
stack = [] # 저장해줄 스택
result = '' # 결과물 출력
cnt = 0 # 괄호 안에 있는지 여부
for i in S : # 받은 문자열 찾아보자
    if i == '<' : # <를 만나면
        cnt = 1 # 지금 괄호 안에 있음 표시
        for _ in range(len(stack)): #괄호 만나기 이전 stack 애들 비워주고 다 뒤집어서 더해!
            result += stack.pop()
    stack.append(i)
    
    if i == '>' : # >를 만나면
        cnt = 0 # 지금 괄호 빠져 나왔음 표시
        for _ in range(len(stack)): # 괄호 안에 있는 애들은 뒤집지 말고 더해!
            result += stack.pop(0)

    if i == ' ' and cnt == 0: # 공백을 만나고 괄호 밖에 있다면
        stack.pop() # 들어간 공백 뺴주고
        for _ in range(len(stack)): # 뒤집어서 더해!
            result += stack.pop()
        result += ' ' # 마지막에 공백 살려주기
print(result)'''