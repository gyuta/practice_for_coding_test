import itertools
import functools

arr = [5,1,3,4,2]
# arr = [2,6,2,8,4,5]

_max = functools.reduce(lambda x, y: x|y, arr)
flg = False
for i in range(1, len(arr)+1):
  for conb in itertools.combinations(arr, i):
    bor = functools.reduce(lambda x, y: x|y, conb)
    if _max == bor:
      print(i)
      flg = True
      break
  if flg:
    break