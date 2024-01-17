lst = []
lst2 = []
for i in range(3):
    lst.append(int(input()))
for i in range(2):
    lst2.append(int(input()))

print(min(lst)+min(lst2) - 50)