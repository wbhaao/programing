import sys
import math
read = sys.stdin.readline
while True:
  num = str(int(read()))
  if (num=="0"): break
  if (str(num[:(len(num)//2)]) == str(list(num[math.ceil(len(num)/2):])[::-1])):
    print("yes")
  else:
    print("no")