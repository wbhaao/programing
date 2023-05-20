stack = []
res = 1
result = 0
p = list(input())

for i in range(len(p)):
    if p[i] == '(':
        res *= 2
        stack.append(p[i])
    elif p[i] == '[':
        res *= 3
        stack.append(p[i])
    elif p[i] == ')':
        if not stack or stack[-1]!= '(':
            result = 0
            break
        if p[i-1]=='(':result+=res
        res //= 2
        stack.pop()
    
    elif p[i] == ']':
        if not stack or stack[-1]!= '[':
            result = 0
            break
        if p[i-1]=='[':result+=res
        res //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)