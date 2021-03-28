import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
  num = int(sys.stdin.readline().rstrip())
  if num % 4 ==0:
    print("Even")
  elif num % 2 ==0:
    print("Same")
  else:
    print("Odd")

