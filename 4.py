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
#########################
import random as r
def proverka(A,B):
    if A == B:
        B = r.randint(1, 9)
w = r.randint(1, 9)
t = r.randint(1, 9)
p = r.randint(1, 9)
while w == t:
    proverka(w, t)
while t == p:
    proverka(t, p)
while w == p:
    proverka(w, p)
o = str(w)+str(t)+str(p)
#########################
if a == w or t or p:
    print(True)
elif b == w or t or p:
    print(True)
elif k == w or t or p:
    print(True)
else:
    print(False)
