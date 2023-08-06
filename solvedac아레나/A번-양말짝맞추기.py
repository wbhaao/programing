lst = []

for i in range(5):
    lst.append(int(input()))
lst.sort()
index = 0
while len(lst)!=1:
    if lst[index] == lst[index+1]:
        del lst[index]
        del lst[index]
    else:
        index += 1
print(lst[0])
        
