a = 0
b = 0
num = float(input('Введите число: '))
while num != 0:
    a += num
    b += 1
    num = float(input('Введите число: '))
print('Сумма: ', a)
print('Количество: ', b)