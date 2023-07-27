import sys
lst = sys.stdin.readline()
stack = 0
result = 0
yet_l = ''
for l in lst:
    if l == '(':
        stack += 1
    if l == ')':
        stack -= 1
        if yet_l=='(':
            result += stack    
        else:
            result += 1
    yet_l = l
print(result)