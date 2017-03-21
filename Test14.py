#coding:utf-8
import math
c = int(raw_input("输入一个整数:"))
List1 = [p for p in range(2,c) if 0 not in [p%d for d in range(2,int(math.sqrt(p))+1)]]
a = c
while a!=1:
    for i in List1:
        if a%i ==0:
            print i,
            a /=i
            break
    if a ==1:
        print '=',
    else:
        print '*',
print c