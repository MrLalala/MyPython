#coding :utf-8
#判断几个某个数是不是满足某个要求
import math
for i in range (10,10000):
    if (math.sqrt(i+100)%1==0) and  (math.sqrt(i+268)%1==0):
        print i

