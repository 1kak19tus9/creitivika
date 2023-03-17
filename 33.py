spisok = []
n = int(input('Сколько чисел? '))
for i in range(n):
    spisok.append(float(input('Введите число: ')))
summa = 0
for elem in spisok:
    summa += elem 
    
print("Среднее арифметическое:", summa/n)