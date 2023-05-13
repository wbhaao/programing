a = [0] * 9
for i in range(9):
  a[i] = int(input())
for i in range(8):
  for z in range(i + 1, 9):
    if sum(a) - a[i] - a[z] == 100:
      del a[z]
      del a[i]
      print(*sorted(a), sep='\n')
      exit()