pole = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', '*', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'], ]

x = 3
y = 4

for stroka in pole:
    for kvadr in stroka:
        print(kvadr, end = ' ')
    print()
command = input("Введи команду: ")
while command != "стоп":
    if x - 1 > 0 and x + 1 < 7 and y - 1 > 0 and y + 1 < 7:
        if command == "пр":
            pole[y][x] = "O"
            x = x + 1
            pole[y][x] = "*"
        elif command == "лв":
            pole[y][x] = "O"
            x = x - 1
            pole[y][x] = "*"
        elif command == "вх":
            pole[y][x] = "O"
            y = y - 1
            pole[y][x] = "*"
        elif command == "нз":
            pole[y][x] = "O"
            y = y + 1
            pole[y][x] = "*"
        else:
            print("Не понял...")
        for stroka in pole:
            for kvadr in stroka:
                print(kvadr, end = ' ')
            print()
    command = input("Введи команду: ")