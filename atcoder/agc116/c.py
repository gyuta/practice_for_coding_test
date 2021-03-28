import functools
import copy
N, M = [int(x) for x in input().split()]
div = 998244353

dic = {i: 1 for i in range(1, M+1)}

div_dic = {}
for i in range(1,M+1):
  for j in range(i, M + 1):
    if i % j == 0:
      div_dic[]
  div_dic[i] = make_divisors(i)
# print(div_dic)

# print(dic)
tmp = copy.copy(dic)
for i in range(N-1):
  for k in range(1,M+1):
    tmp[k] = functools.reduce(lambda x,y: (x + dic[y]) % div , div_dic[k],0 )
  dic = copy.copy(tmp)

_sum = 0
for item in dic.values():
  _sum += item
  _sum %= div
print(_sum)
