#coding:utf-8

#输出99乘法表

#正常方式使用的是%占位
for i in range(1,10):
    for j in range(1,i+1):
        print "%d * %d = %d" % (i,j,i*j) ,
    print


#使用format格式再来一次
#format 使用的是｛｝占位
for i in range(1,10):
    for j in range (1,i+1):
        print "{} * {} = {}".format(i,j,i*j),
    print