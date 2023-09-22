class ch():
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
    def sum(self):
        print(self.one+self.two+self.three)
on = int(input())
tw = int(input())
thre = int(input())
a = ch(on,tw,thre)
a.sum()