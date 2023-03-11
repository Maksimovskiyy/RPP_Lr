import sys
print((sys.argv))

print(min(sys.argv))
y = sys.argv
res = [i for i, j in enumerate(y) if j == min(y)]
print(res)
print (*filter(lambda x: x >= '0', y))
print (*filter(lambda x: x < '0', y))