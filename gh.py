num = int(input())
def t(num):
    if num == 1:
        print (1)
        return 1
    else:
        print(num)
        return t(num - 1) 
t(num)   