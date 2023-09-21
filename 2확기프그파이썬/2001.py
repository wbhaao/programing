lst = []
lst1 = []
for i in range(3):
    lst.append(int(input()))
for i in range(2):
    lst1.append(int(input()))

print(round(min(lst)+min(lst1)+(min(lst)+min(lst1))/10, 1))