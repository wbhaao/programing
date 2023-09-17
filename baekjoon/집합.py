import sys
input = sys.stdin.readline

N = int(input())
lst = set()
for _ in range(N):
  arr = list(input().split())
  c = arr[0]
  if c == "add":
    lst.add(int(arr[1]))
  elif c == "remove":
    try:
      lst.remove(int(arr[1]))
    except:
      pass
  elif c == "check":
    if int(arr[1]) in lst:
      print(1)
    else:
      print(0)
  elif c == "toggle":
    if int(arr[1]) in lst:
      lst.remove(int(arr[1]))
    else:
      lst.add(int(arr[1]))
  elif c == "all":
    lst = set([i for i in range(1,21)])
  else:
    lst = set()
