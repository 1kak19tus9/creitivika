a = int(input())
if a % 3 == 0 and a > 0:
    print("a кратно 3 и больше 0")
elif a % 3 == 0 and a < 0:
    print("a кратно 3 и меньше 0")
elif a % 3 != 0 and a < 0:
    print("a некратно 3 и меньше 0")
elif a % 3 != 0 and a > 0:
    print("a некратно 3 и больше 0")
else:
    print("a походу 0")