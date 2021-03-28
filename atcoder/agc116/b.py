import sys
div = 998244353
N = int(sys.stdin.readline().rstrip())
A = [int(x) for x in sys.stdin.readline().rstrip().split()]
A.sort()
# print(A)
ans = 0
_sum = 0
former = 0
for i in A:
  ans += (i*i) % div
  ans %= div

  _sum = (_sum * 2 + former) % div

  ans += (i*_sum) % div
  ans %= div

  former = i

print(ans)