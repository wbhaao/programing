N, r, c = map(int, input().split())
answer = 0
2
row = [1, 2, 1, 2+8, 1, 2, 1, 2+8+32, 1, 2, 1, 2+8, 1, 2, 1, 2+8+32+128, 1, 2, 1, 2+8, 1, 2, ]
for i in range(1, 2**N+1):
    if i%2 == 1:
        row.append(1)
    
colunm = [2, 6, 2, 22, 2, 6, 2, 86, 2, 6, 2, 22, 2, 6, 2]
for i in range(c):
    answer += row[i]
for i in range(r):
    answer += colunm[i]
print(answer)
