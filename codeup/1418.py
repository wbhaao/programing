a = input()
tIndexs = []
for i, s in enumerate(a):
    if s=='t':
        tIndexs.append(i)
for i in tIndexs:
    print(i+1, end=" ")