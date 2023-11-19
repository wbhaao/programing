n = int(input())

number = 0
for i in range(1, n+1):
    number += i

for i in range(1, n+1):
    for j in range(0, i):
        print(f"{number}", end=" ")
        number -= 1
    print("")