import itertools
import functools

# arr = [5,1,3,4,2]
arr = [2,6,2,8,4,5]

max_value = 0
min_size = len(arr)
dic = {}
for i in reversed(range(1, len(arr)+1)):
  for conb in itertools.combinations(arr, i):
    bor = functools.reduce(lambda x, y: x|y, conb)
    print(conb, bor, max_value, min_size)
    if bor >= max_value:
      max_value = bor
      if i < min_size:
        min_size = i
print(min_size)
    