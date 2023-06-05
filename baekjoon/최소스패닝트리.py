node, line = map(int, input().split())
a = []
for i in range(line):
    a.append(list(map(int, input().split()))[2])

a.sort()
print(sum(a[:line+(node-line)-1]))
