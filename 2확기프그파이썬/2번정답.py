n = int(input())
def func(n):
  print(n)
  if(n!=1):
    func(n-1)
func(n)