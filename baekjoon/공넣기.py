N, M = map(int, input().split())
box = [0] * N

for _ in range(M) :
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        box[i-1] = C

print(*box)