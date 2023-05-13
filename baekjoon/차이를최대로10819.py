a = int(input())
b = list(map(int, input().split()))
c = 0
f = 0
y = 0
s = 0

b.sort()
d = b[0:a//2]
e = b[a//2:]
e.sort(reverse=True)
e[0], e[len(e)-1] = e[len(e)-1], e[0]
d.insert(1, e[len(e)-1])
del e[len(e)-1]
for i in range(a-1):
    try:c += abs(e[i] - d[i])
    except: pass
    try:c += abs(d[i] - e[i+1])
    except: pass
    
    
d = b[0:a//2]
e = b[a//2:]
e.sort(reverse=True)
d[0], d[len(d)-1] = d[len(d)-1], d[0]
d.insert(1, d[len(d)-1])
del d[len(d)-1]
for i in range(a-1):
    try:f += abs(d[i] - e[i])
    except: pass
    try:f += abs(e[i] - d[i+1])
    except: pass
    
d = b[0:a//2+1]
e = b[a//2+1:]
e.sort(reverse=True)
d[0], d[len(d)-1] = d[len(d)-1], d[0]
d.insert(1, d[len(d)-1])
del d[len(d)-1]
for i in range(a-1):
    try:y += abs(d[i] - e[i])
    except: pass
    try:y += abs(e[i] - d[i+1])
    except: pass
        
d = b[0:a//2+1]
e = b[a//2+1:]
e.sort(reverse=True)
e[0], e[len(e)-1] = e[len(e)-1], e[0]
e.insert(1, e[len(e)-1])
del e[len(e)-1]
for i in range(a-1):
    try:s += abs(e[i] - d[i])
    except: pass
    try:s += abs(d[i] - e[i+1])
    except: pass
    
print(max([c, f, y, s]))