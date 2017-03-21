#coding:utf-8
import math

d = [i for i in range(2,100) if 0 not in [i%p for p in range(2,int(math.sqrt(i))+1)]]
print d

#方法2
for i in range(2,200):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            break
    else:
        print i,