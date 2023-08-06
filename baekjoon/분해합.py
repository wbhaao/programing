N = int(input())
for i in range(1, N):
    result = i
    for letter in str(i):
        result += int(letter)
    if result == N:
        print(i)
        exit()
print(0)
