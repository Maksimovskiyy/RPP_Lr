mas = [int(x) for x in input().split()]
print(mas)
print(min(mas))
res = [i for i, j in enumerate(mas) if j == min(mas)]
print(res)
print(*filter(lambda x : x > 0, mas))
print(*filter(lambda x : x < 0, mas))
