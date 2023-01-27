a = input("Введите пароль:")
def nc(parol):
    ncp = False
    for i in parol:
        if i >= "0" and i <= "9":
            ncp = True
    return ncp
def bc(parol):
    ncb = False
    for i in parol:
      if  i >= "a" and i <= "z":
          ncb = True
    return ncb
def sc(parol):
    nsc = False
    for i in parol:
        f = ['!','&','@','%','^','$','?','#','№']
        if i in f:
            nsc = True
            return nsc
print(nc(a))
prirnt