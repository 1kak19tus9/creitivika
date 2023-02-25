n =  int(input())
def vi(n):
    if n == 1:
        return 1
    else:
       return n, vi(n-1)
print(vi(n))