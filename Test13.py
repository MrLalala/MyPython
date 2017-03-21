#coding:utf-8

import math
import random

for i in range(100,1000):
    a = i/100
    b = i%100/10
    c = i%10
    if math.pow(a,3)+math.pow(b,3)+math.pow(c,3)==i:
        print i
    if a**3+b**3+c**3 ==i:
        print i