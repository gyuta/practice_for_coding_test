import itertools
import functools

arr = [5,1,3,4,2]
# arr = [2,6,2,8,4,5]

dic = {}
for i in range(1, len(arr)+1):
  for conb in itertools.combinations(arr, i):
    bor = functools.reduce(lambda x, y: x|y, conb)
    print(conb, bor, dic)
    if bor not in dic:
      dic[bor] = i

_max = functools.reduce(lambda x, y: x|y, arr)
print(_max)
print(dic[_max])
    