a = input()
a1 = 0
a2 = 0
back = False
for i in a:
    if i=='c' or i=='C':
        a1 += 1
        if back:
            a2 += 1
        back = True
    else:
        back = False
print(a1)
print(a2)
