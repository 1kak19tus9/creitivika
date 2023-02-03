import random as r
def proverka(A,B):
    if A == B:
        B = r.randint(1, 9)
a = r.randint(1, 9)
b = r.randint(1, 9)
k = r.randint(1, 9)
while a == b:
    proverka(a, b)
while b == k:
    proverka(b, k)
while a == k:
    proverka(a, k)
g = str(a)+str(b)+str(k)
print(g)