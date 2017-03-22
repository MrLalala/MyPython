#coding:utf-8

#非nab序列
List = []
# def fn(i):
#     fn(0) = 1
#python的递归函数：
def fn(i):
    if i ==0 or i ==1:
        return 1
    return fn(i-1)+fn(i-2)

for i in range(10):
    List.append(fn(i))
print List
#访法2：
def fn2(i):
    a,b = 1,1
    for i in range(i-1):
        a,b = b,a+b
    return b

for i in range(10):
    List.append(fn(i))
print List

def func():
    if i ==0:
        return 1
    elif i == 1:
        return 1
    else:
        return fn(i-1)+fn(i-2)
#访法2：
    
for i in range(10):
    List.append(fn(i))

print List

