person = {"name": "Илья Павлович Гашев", "math 4; PE 5; English 4; Art 5"}
while True:
    a = input("Choose command:new property or remake or exit:")
    if a == "remake":
        b = input("Choose item:")
        c = int(input("Wright remake:"))
    elif a == "new property":
        d = input("Wright item:")
        e = int(input("Wright meaning:"))
        person[d] = e
    elif a == "exit":
      break
    else:
       a = input("Choose command:new property or remake:")
print(person and lessons)
