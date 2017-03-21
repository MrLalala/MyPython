#coding:utf-8

#古典问题：菲纳波兔子？？？
#
# def fn(i):
#     if i ==1 or i == 2:
#         return 1
#     return fn(i-1)+fn(i-2)
#
# for i in range(1,43):
#     print "%12ld" %fn(i),
#     if i %6 == 0:
#         print
#
#递归耗时太长，不建议使用
f1 = 1
f2 = 1

for i in range(1,22):
    print "%12ld%12ld" %(f1,f2),
    if(i%3 == 0):
        print
    f1 = f1+f2
    f2 = f1+f2
