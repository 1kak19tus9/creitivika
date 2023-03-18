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
for i in range(5):
    e = random.randint(1,12)
    t = random.randint(1,12)
bombik = 5
for i in range(bombik):
    e = random.randint(1,11)
    t = random.randint(1,11)
    pole[e][t] = "&"
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
   

    for stroka, strokaSMinami in (vidimost_polya, pole):
      

        if stroka.count("*") == len(stroka) - strokaSMinami.count("&"):
            print("pobeda")
            return False
    
    return opened







def bomb(x, y):
    cnt = 0
    for i in range(-1,1):
        for j in range(-1,1):
            if (pole[y+i][x+j] == "&"):
                cnt += 1
    return cnt

b = int(input("Введите координату х:"))
c = int(input("Введите координату у:"))
a = input("Введите команду(флажок/поле):")



if a == "флажок":
    pole[b][c] = "@"
elif a == "поле":
    pole[b][c] = pole
    
    
for i in range(len(pole)):
    for j in range(len(pole[i])):
        if (pole[i][j] == '#'):
            pole[i][j] = bomb(i,j)
for i in range(len(pole)):
    for j in range(len(pole[i])):
        print(pole[i][j], end=" ")
    print()
    