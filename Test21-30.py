#coding:utf-8


#Test-21:猴子吃桃
def monkey():
    num = 1
    for i in range(9):
        num +=1
        num *=2
    print num

#Test-22:比赛判断问题
# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
def ref():
    for i in range(ord('x'),ord('z')+1):
        for j in range (ord('x'),ord('z')+1):
            if i!=j:
                for k in range (ord('x'),ord('z')):
                    #print i,j,k
                    #感觉思路应该是先找到互不相同的，再从中挑选符合条件的
                    #但是如果直接谢三重循环的话，感觉太占用时间，
                    #所以在二重循环后添加一个判断，这样可以节省代码时间
                    if (i!=k) and (j!=k) :
                        print i, j, k
                        if(i != ord('x')) and (k!=ord('x'))and (k!=ord('z')):
                            print 'order is a -- %s\t b -- %s\tc--%s' \
                                  % (chr(i),chr(j),chr(k))
#Test-23：输出菱形
def put(i):
    f = 1
    j = 1
    while j>0:
        for a in range(i-j,-1,-1):
            print ' ',
        for k in range(1,2*j):
            print '*',
        if j == i :
            f = -1
        j+=f
        print

#Test-24：求某一分数列的和
def sumF():
    a = 1.0
    b = 2.0
    sumq = 0
    for i in range (20):
        sumq += b / a
        a,b = b,a+b
    print sumq
#sumF()
#put(11)
#ref()
#monkey()

