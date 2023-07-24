n = int(input())
lst = ['A', 'B', 'C', 'D', 'F']
for i in range(5):
    if i == 4:
        print(lst[i])
        break
    if n>=90-i*10:
        print(lst[i])
        break