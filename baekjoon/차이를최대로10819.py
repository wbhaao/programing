a = int(input())
b = list(map(int, input().split()))
c = 0
f = 0

b.sort()
d = b[0:a//2]
e = b[a//2:]
e.sort(reverse=True)
e[0], e[len(e)-1] = e[len(e)-1], e[0]
for i in range(a//2):
    c += abs(e[i] - d[i])
    if i!=a//2-1:c += abs(d[i] - e[i+1])
    
d = b[0:a//2]
e = b[a//2:]
e.sort(reverse=True)
d[0], d[len(d)-1] = d[len(d)-1], d[0]
for i in range(a//2):
    f += abs(d[i] - e[i])
    if i!=a//2-1:f += abs(e[i] - d[i+1])
    
print(max(c, f))