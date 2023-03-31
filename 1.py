w = 5
person = {"name": "Jake", "age": 18, "height": 194, "eyes": "brown", "zodiac sign": "scales", "country": "France"}
while w == 5:
    a = input("Choose command:new property or remake or exit:")
    if a == "remake":
        b = input("Choose item:")
        c = input("Wright remake:")
    elif a == "new property":
        d = input("Wright item:")
        e = input("Wright meaning:")
        person[d] = e
    elif a == "exit":
      w = 6
    else:
       a = input("Choose command:new property or remake:")
print(person)