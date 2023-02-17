def findMedianSortedArrays(nums1, nums2):
    i ,j= 0 ,0
    if len(nums1)<len(nums2): 
        temp=nums1;nums1=nums2;nums2=temp
    temp = []
    while True:
        if i+1>len(nums1) or j+1>len(nums2): break
        if nums1[i]>nums2[j]:
            temp.append(nums2[j])
            j+=1
        else: 
            temp.append(nums1[i])
            i+=1
    temp+=nums1[i:]
    temp+=nums2[j:]

    if len(temp)%2: return float(temp[len(temp)//2])
    else: return (temp[len(temp)//2]+temp[len(temp)//2-1])/2


x = findMedianSortedArrays([1,3], [2])















'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


l1 = None
l1 = ListNode(1,l1)
l1 = ListNode(9,l1)
l3 = ListNode(9)
l3 = ListNode(8,l3)
l3 = ListNode(1,l3)

def check_deep(l1):
    depth = 1
    while True:
        if l1.next == None: return depth
        else: l1=l1.next;depth+=1
    
def reverse(l1):
    l2 = None
    while True:
        l2 = ListNode(l1.val,l2)
        if l1.next==None:
            break
        l1 = l1.next

    return l2

def pr(l1):
    while True:
        print(l1.val)
        if l1.next == None: break
        else: l1=l1.next

# print(check_deep(l1))
def addTwoNumbers(l1,l2):
    depth = max(check_deep(l1),check_deep(l2))
    if check_deep(l1)!=depth: temp=l1;l1=l2;l2=temp
    l3 = None;
    for i in range(depth):
        l3 = ListNode(l1.val+l2.val,l3)
        if l2.next == None:
            l2.val = 0
        else: l2=l2.next
        l1=l1.next
        if l3.val>9: l2.val+=1;l3.val-=10
    if l2.val>0: l3 = ListNode(1,l3)
    return l3


pr(reverse(addTwoNumbers(l1,l3)))

'''
'''
from PIL import Image, ImageDraw
  
images = []

for i in range(11,18):
    images.append(Image.open('Figure_'+str(i)+'.png'))
images[0].save('total.gif',
               save_all = True, append_images = images[1:], 
               optimize = False, duration = 1000)


'''
'''
import matplotlib.pyplot as plt
import numpy as np
import random

x=np.linspace(0,10,100)
print(x)
n = []
for i in range(10):
    n.append(random.randint(0,10))

m = {'pa':1,'pl':2}
#plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.plot(x,m)
#plt.title('标题')
plt.show()

'''
