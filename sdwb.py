# 十步万度求解器
import matplotlib.pyplot as plt

class Matrix():
    def __init__(self,i,j):
        self.x = j
        self.y = i
        self.total = 0
        self.matrix = []
        self.set_array()
    def set_array(self):
        for i in range(self.y):
            self.matrix.append([])
            for j in range(self.x):
                self.matrix[i].append(0)
    def choose(self,i,j):
        if i<0 or j<0 or i>self.y-1 or j>self.x-1: return 0
        self.matrix[i][j]=(self.matrix[i][j]+1)%4
        self.total+=1
        if self.matrix[i][j] == 0:
            self.choose(i-1,j)
        elif self.matrix[i][j] == 1:
            self.choose(i,j+1)
        elif self.matrix[i][j] == 2:
            self.choose(i+1,j)
        elif self.matrix[i][j] == 3:
            self.choose(i,j-1)
        return 0
    def pr_m(self):
        for i in self.matrix:
            print(i)
        # print('--------------------------------\n')
    def sequence(self):
        l = []
        for i in range(self.y):
            for j in range(self.x):
                l.append([i,j])
        return l
    def inital(self):
        self.total = 0
        self.matrix = []
        self.set_array()
        

x = Matrix(4,3)



def delet(l1, l2):
    temp = [i for i in l1]
    for i in l2:
        temp.remove(i)
    return temp

d = 1
l1 = []
n=0
title = []
score = []
maximum = 0
def ct(x,deep,m):
    global l1
    
    for i in x.sequence():
        l1.append(i)
        if deep == m:
            check(x,l1)
            x.inital()
        else: ct(x,deep+1,m)
        l1.remove(i)
        

def check(x,sequence):
    global n,maximum
    n+=1
    for l in sequence:
        x.choose(l[0],l[1])
    if x.total*90>maximum: maximum=x.total*90
    if x.total*90 not in title: title.append(x.total*90);score.append(0)
    score[title.index(x.total*90)]+=1
    
    #print('-------------'+str(n)+'-------------')
    #print(x.total*90)
    #x.pr_m()
for i in range(1,6):
    ct(x,d,i)
    plt.scatter(title,score)
    print(title)
    print(score)
    title = []
    score = []
plt.show()
