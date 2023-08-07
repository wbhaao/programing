N = int(input())
string = input()
answer = 0
for i, s in enumerate(string):
    answer += (ord(s) - 96) * (31**i)
print(answer % 1234567891)
