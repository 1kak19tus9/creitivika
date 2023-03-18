import mylib

mylib.vyvodPolya(mylib.vidimost_polya)
game = True
while game:
    stroka = int(input("Введите номер строки"))
    stolb = int(input("Введите номер столбца"))
    while stroka <= 1 or stroka >= 12 or stolb <= 1 or  stolb >= 12:
            stroka = int(input("Введите номер строки"))
            stolb = int(input("Введите номер столбца"))
    mylib.check(stroka-1,stolb-1)
    mylib.vyvodPolya(mylib.vidimost_polya)
    if mylib.isOpen():
        game = False


print("Всё поле открыто!")