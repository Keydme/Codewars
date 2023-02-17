# 引用所需要的库
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义画布
fig, ax = plt.subplots()
line, =ax.plot([], [])
#line1, = ax.plot([], [])  # 返回的第一个值是update函数需要改变的
#line2, = ax.plot([], [])


# 获取直线的数组
def line_space(x1, x2, B, C, A):
    x = np.linspace(x1, x2, B)
    return x, np.sin(A*(x+C))

def addy(B):
    x = np.linspace(0, 20, 1000)
    y = np.linspace(0,0,1000)
    x1, y2 = line_space(20-20*B/1000, 20, B+1, 20*B/1000-20, 1)#+np.pi)
    x2, y1 = line_space(0, 20*B/1000, B+1, -20*B/1000, 2)
    if B>500: 
        for i in range(1000-B,B):
            y[i]=y1[i]+y2[i-1000+B]
        for i in range(1000-B):
            y[i]=y1[i]
            y[-i-1]=y2[-i-1]
    else:
        for i in range(B):
            y[i] = y1[i]
            y[-i-1]=y2[-i-1]
    return x, y


# 这里B就是frame
def update(B):
    ax.set_xlim(0, 20)
    ax.set_ylim(-2, 2)
    #x1, y1 = line_space(20-20*B/1000,20,1000-B)
    #x2, y2 = line_space(0,20*B/1000,B)
    x, y = addy(B)
    line.set_data(x, y)
    #line1.set_data(x1,y1)
    #line2.set_data(x2,y2)
    return line#[line1,line2]

# 使用函数并保存保存会在下一篇文章讲
# 可以用plt.show()来代替一下

#addy(15)

ani = FuncAnimation(fig, update, frames=range(1000), interval=10)
ani.save('move1.mp4', fps=100)
