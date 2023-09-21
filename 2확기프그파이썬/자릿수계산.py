n = int(input())
def get_max_num(n):
    num = 0
    for i in range(1, n+1):
        num += i
    return num

number = get_max_num(n)

for i in range(1, n+1):
    for j in range(0, i):
        print(number, end=' ')
        number -= 1
    print()