def hanoi_tower(n, source, target, auxiliary):
    if n > 0:
        hanoi_tower(n-1, source, auxiliary, target)
        print(f"Disk {n} : {source} to {target}")
        hanoi_tower(n-1, auxiliary, target, source)

n = int(input())
hanoi_tower(n, 'A', 'C', 'B')
