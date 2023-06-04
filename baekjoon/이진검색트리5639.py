lst = []
while True:
    try:
        lst.append(int(input()))
    except:
        break

root = int(lst[0])

lst.sort()
n = int(lst[0])
i = 0
iss = True
while root>lst[i]:
    print(lst[i])
    if iss: 
        i+=2 
        if i!=2:
            i += 1
        iss = not iss
    else: i-=1; iss = not iss

lst.sort(reverse=True)
i = 0
iss = True
while root<lst[i]:
    print(lst[i])
    if iss: 
        i+=2 
        if i!=2:
            i += 1
        iss = not iss
    else: i-=1; iss = not iss