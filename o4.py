su = 0
print("Введите число и мы посчитаем сумму всех чисел 1, 2, 3 ... num")
num = int(input('Введите целое число: '))
for i in range(1, num+1):
    su = su + i
print('Сумма всех чисел от 1 до', num, '—', su)