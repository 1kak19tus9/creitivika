class ch():
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
    def sum(self):
        d = (self.one+self.two+self.three)
        if d == 1500 or d > 1500:
            print('да будут шашлыки')
        else:
            print('сидите дома водичку пейте')
on = float(input())
tw = float(input())
thre = float(input())
a = ch(on,tw,thre)
a.sum()