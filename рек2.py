A = int(input())
B = int(input())


def t1(A, B):
    print(A)
    if A < B:
        t1(A+1, B)
    

def t(A, B):
    print(B)
    if A > B:
        t(A, B-1)



if A<B:
    t1(A,B)
else:
    t(A,B)


        