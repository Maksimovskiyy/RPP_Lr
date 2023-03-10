String = input("Введите строку: ")
x = String.replace(":", "%")
print(x)
col = 0
for i in String:
    if i == ':':
        col += 1
print(col)

