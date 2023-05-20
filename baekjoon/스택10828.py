import sys

n = int(sys.stdin.readline())

lst=[]

for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0]=='push':
        lst.append(cmd[1])
    elif cmd[0]=='pop':
        if len(lst)==0:
            print(-1)
        else:
            print(lst.pop())
    elif cmd[0] == 'size':
        print(len(lst))
    elif cmd[0] == 'empty':
        if len(lst)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(lst)==0:
            print(-1)
        else:
            print(lst[-1])