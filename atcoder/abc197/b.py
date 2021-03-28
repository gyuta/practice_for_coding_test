from sys import stdin

H, W, X, Y = [int(x) for x in stdin.readline().rstrip().split()]

S = [stdin.readline().rstrip() for i in range(H)]

i = X - 1
j = Y - 1
count = 0
## left
a = i
b = j
while b >= 0 and S[a][b] != '#':
  count += 1
  b -= 1

# right
a = i
b = j
while  b < W and S[a][b] != '#':
  count += 1
  b += 1

# top
a = i
b = j
while a >= 0 and S[a][b] != '#':
  count += 1
  a -= 1


# bottom
a = i
b = j
while a < H and S[a][b] != '#':
  count += 1
  a += 1

print(count - 3)

  