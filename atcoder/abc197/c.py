from sys import stdin
import functools


def xor(_list):
  return functools.reduce(lambda a, b: a ^ b, _list)

def list_or(_list):
  return functools.reduce(lambda a, b: a | b, _list)

N = int(stdin.readline().rstrip())

a = [int(x) for x in stdin.readline().rstrip().split()]

_min = functools.reduce(lambda x, y: x | y, a)
for bit in range(2**(N-1)):

  divids = []
  for i in range(N-1):
    if bit & (1 << i):
      # print(i)
      divids.append(i)
  divids.append(N-1)
  
  pattern = []
  left = 0
  for right in divids:
    pattern.append(a[left: right+1])
    left = right + 1

  # print(divids, pattern)
  ors = [list_or(item) for item in pattern]
  value = xor(ors)

  if _min > value:
    _min = value
print(_min)
