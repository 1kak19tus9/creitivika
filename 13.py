tin = {"tin":30}
biba = {"biba":24}
null = {"null":0}
a = input("введите ник: ")
b = int(input("введите число: "))
aba = {a:b}
rec = [tin,biba,aba]
print(rec)
print(list(rec[2].values()))
if list(rec[2].values())[0] >= list(rec[1].values())[0]:
    null = rec[2]
    rec[2] = rec[1]
    rec[1] = null
print(rec)
print(list(rec[1].values()))
if list(rec[1].values())[0] >= list(rec[0].values())[0]:
    null = rec[1]
    rec[1] = rec[0]
    rec[0] = null
print(rec)