print("Вот и закончились летние каникулы, вы вновь в школе чародейства и волшебства 'Хогвартс'")
gender = input("Выберите ваш пол: девушка, парень: ")
while
gender != "парень" and "девушка":
    gender = input("Выберите ваш пол: девушка, парень: ")
if gender == "девушка":
    name = in
faculty = input("выберите: Пуффендуй, Гриффиндор, Когтевран, Слизерин: ").lower()
while 
faculty != "Пуффендуй" and faculty != "Когтевран" and faculty != "Гриффиндор" and faculty != "Слизерин":
    faculty = input("выберите: Пуффендуй, Гриффиндор, Когтевран, Слизерин: ").lower()
if faculty == "Пуффендуй":
    print("К вам подлетает одногрупник с объятиями, говоря что после всего в гостиной будет тёплый приём первокурсников и будут кексики с ликёром")
    action = input("выберите: пройти в комнату").lower()
    while action != "пройти в комнату":
        action = input("выберите:пройти в комнату: ").lower()
    if action == "пройти в комнату":
        print("")
        print("Он вас съел")
        print("Game over")
    else:
        print("Вы видите корону")
        vybor = input("Выберите: надеть или не надевать: ").lower()
        while vybor != "надеть" and vybor != "не надевать":
           vybor = input("Выберите: надеть/не надевать": ).lower()
        if vybor == "надеть":
            print("В подвал врывается дракон, но вы уже в короне и его правитель")
            print("Вам с драконом предстоит много замечательных приключений")
            print("С победой!")
        else:
            print("В подвал врывается дракон и съедает вас")
            print("Game over")
elif vybor == "налево":
    print("Вас встретил дракон и съел")
    print("Game over")
else:
    print("Вы вышли из замка и услышали сзади грозный рык")
    print("Вы пытались убежать от дракона, но он быстрее и сильнее")
    print("Game over")