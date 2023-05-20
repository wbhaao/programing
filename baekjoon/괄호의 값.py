stack = [] # 스택
res = 1 # result에 더해주기 전 임시 변수
result = 0 # 결과 변수
p = list(input()) # 입력값

# 1~4번째 과정 시작
for i in range(len(p)):
  # 바로 2를 곱한다
  if p[i]=='(':
    res *= 2
    stack.append(p[i])
  # 바로 3을 곱한다
  elif p[i]=='[':
    res *= 3
    stack.append(p[i])

  elif p[i]==')':
    # stack의 끝과 짝이 맞지 않거나 stack이 비었다면
    if not stack or stack[-1]!='(':
      result = 0
      break
    # 내 뒤에꺼가 (라서 더해야 하는 상황이라면
    # 이건 합으로 계산될때 +를 해주고 곱일때는 중간에 뭐가 꼽사리 껴있으니까 딴거 곱하기 해준걸로 만족하고 퇴장한다
    if p[i-1]=='(': result += res
    # 짝을 받을때 곱했던 2는 회수
    # 곱 역할을 하는 괄호가 사라져서 /2를 해준다!!!!!!!!!!!!!
    res //= 2
    stack.pop()
    
  elif p[i]==']':
    if not stack or stack[-1]!='[':
      result = 0
      break
    if p[i-1]=='[': result += res
    res //= 3
    stack.pop()


# 결과 출력
if stack:
  print(0)
else:
  print(result)