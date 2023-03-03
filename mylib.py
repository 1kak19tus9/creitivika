import random

pole = [["*","*","*","#","*","*","*","*","*","*","*","*"],
         ["*","*","*","#","*","*","*","*","*","*","*","*"],
         ["*","*","*","#","*","*","*","*","*","*","*","*"],
         ["*","*","*","#","*","*","*","#","#","#","#","#"],
         ["*","*","*","#","#","#","#","#","*","#","*","*"],
         ["*","*","*","#","*","*","*","*","*","#","*","*"],
         ["#","#","#","#","*","*","*","*","*","#","#","#"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
         ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"]]

vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"]]
bombik = 5
for i in range(bombik):
    e = random.randint(1,11)
    t = random.randint(1,11)
    vidimost_polya[e][t] = "&"
def vyvodPolya(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end='')
        print()

def check(stroka,stolb):
    if vidimost_polya[stroka][stolb] == "•":

        vidimost_polya[stroka][stolb] = pole[stroka][stolb]

        if pole[stroka][stolb] == "*":

            if stroka-1 >= 0:
                check(stroka-1,stolb)
                if stolb-1 >= 0:
                    check(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka-1,stolb+1)

            if stroka+1 < len(pole):
                check(stroka+1,stolb)
                if stolb-1 >= 0:
                    check(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka+1,stolb+1)

            if stolb-1 >= 0:
                    check(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                check(stroka,stolb+1)

def isOpen():

    opened = True

    for stroka in vidimost_polya:

        if "•" in stroka:

            opened = False
        else:
            opened = True
            print("Игра окончена")
    return opened
def bomb():
    if stroka +1 == 
        

