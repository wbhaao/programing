import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    string = input().split()
    for letter in string:
        print(letter[::-1], end=" ")