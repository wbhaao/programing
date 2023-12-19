#-*- coding:utf-8 -*-

def beautify(code):
  prev = code[0]
  res = []
  block = [prev, 0]
  w = ".,[]"
  
  for i in range(len(code)):
    c = code[i]
    if prev == c: block[1] += 1
    else:
      res.append(block)
      prev = c
      block = [prev, 1]
  if block: res.append(block)
  
  for i in range(len(res)):
    t, c = res[i]
    if t in w:
      R = [[t, 1]]*c
      res = res[:i] + R + res[i+1:]

  return res

def loopfind(code):
  c = beautify(code)
  result = {}
  res = []
  for i in range(len(c)):
    if c[i][0] == "[": res.append(i)
    if c[i][0] == "]":
      p = res.pop()
      result[p] = i
      result[i] = p
  return result

def bf2um(code, debug=False):
  vars = []
  resl = ["어떻게", ""]
  result = []
  offset = 3
  point = 1
  loops = loopfind(code)
  b = beautify(code)
  r = range(len(b))

  for i in r:
    var = getUmPointer(point)
    t, c = b[i]
    if t in "><":
      point += 2*int(b[i][0]==">")-1
    if t in "+-" and not point in vars:
      vars.append(point)
      resl.append(f"{var[:-1]}엄")
      offset += 1
  point = 1
  for i in r:
    var = getUmPointer(point)
    res = ""
    t, c = b[i]
    if t == "+": res = f"{var[:-1]}엄{var}{'.'*c}"
    if t == "-": res = f"{var[:-1]}엄{var}{','*c}"
    if t == ">": point += c
    if t == "<": point -= c
    if t == ".":
      res = f"식{var}ㅋ"
    if t == ",": res = f"{var[:-1]}엄식?"
    if t == "[":
      n = loops[i]+2+offset
      res = f"동탄{var}?준{n if debug else getUmNumber(n)}"
    if t == "]":
      n = loops[i] + 1 + offset
      res = f"준{n if debug else getUmNumber(n)}"
    result.append(res)

  realres = resl + [""] + result + ["", "화이팅!.,", "", "이 사람이름이냐ㅋㅋ"]
  return '\n'.join(list(map(
    lambda x: f"{str(x+1)+' : ' if debug else ''}{realres[x]}",
    range(len(realres))
  )))

def getUmPointer(p): return "어"*p

from primeUtils import Factorize
def getUmNumber(n):
  res = []
  f = Factorize(n)
  for i in f.keys():
    for j in [i]*f[i]:
      res.append("."*j)
  return ' '.join(res)