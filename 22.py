twolist = []
def make2(twonk, twolist):
    if twonk >= 2:
        twolist.insert(0, int(twonk))
        make2(twonk/2, twolist)
        
make2(1024, twolist)
print(twolist)