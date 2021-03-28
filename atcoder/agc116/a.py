import sys

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

T = int(sys.stdin.readline().rstrip())
for i in range(T):
  num = int(sys.stdin.readline().rstrip())
  _list = make_divisors(num)
  count = 0
  for item in _list:
    count += 1 if item % 2 ==0 else -1
  if count == 0:
    print("Same")
  elif count > 0:
    print("Even")
  else:
    print("Odd")

