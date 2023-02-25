# Задание 3
m = float(input('Введите вещественное число: '))
for x in range(1, 11):
    print(x*m)
# Задание 4
a = 0
b = 0
num = int(input('Введите число: '))
while num != 0:
    a += num
    b += 1
    num = int(input('Введите число: '))
print('Сумма: ', a)
print('Количество: ', b)