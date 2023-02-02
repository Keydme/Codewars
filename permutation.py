from time import time


def delet(l1, l2):
    temp = [i for i in l1]
    for i in l2:
        temp.remove(i)
    return temp


class Permu():

    def __init__(self, s):
        self.s = s
        self.length = len(s)
        self.d = 0
        self.temp = ''
        self.fp = []

    def f(self, s):
        self.d += 1
        for i in s:
            self.temp += i
            #print(i, self.d, self.temp)
            self.f(delet(s, [i]))
            self.temp = self.temp[0:-1]
            #print('-', self.d, self.temp)
        if self.length + 1 == self.d:
            self.fp.append(self.temp)
            #print('1111111111')
        self.d -= 1


x = Permu('1122')
t1 = time()
x.f(x.s)
t2 = time()
print(x.fp)
print(len(x.fp), len(set(x.fp)))
print(t2 - t1)
