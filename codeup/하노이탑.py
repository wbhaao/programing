def hanoi(n, source, target, helper):
    if n > 0:
        hanoi(n-1, source, helper, target)
        print(f'Disk {n} : {source} to {target}')
        hanoi(n-1, helper, target, source)

n = int(input())

def hanois(n, o, t, th):
    if n > 0:
        hanoi(n-1, o, th, t)
        print(f'Disk {n} : {o} to {t}')
        hanoi(n-1, th, t, o)

hanois(4, 'A', 'C', 'B')