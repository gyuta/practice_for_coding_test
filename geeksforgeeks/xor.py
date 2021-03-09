arr = [0]
arr.append(4)
arr.append(2)
arr = list(map(lambda x: x^4, arr))
arr.append(5)
arr = list(map(lambda x: x^8, arr))
print(sorted(arr))