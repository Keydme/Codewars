import os
from urllib.request import urlretrieve as downl

out = os.popen("node "+input('name:'),'r').read()

#scope = {}

out=eval(out)
#do2=exec('a='+out,scope)

print(out)
n = 1

for i in out:
    i = i[:i.index('=s')+2]+'0'+i[i.index('?'):]
    # print(i)
    downl(i,"hq_"+str(n)+'.jpg')
    print('complete '+str(n)+'.jpg')
    n+=1
