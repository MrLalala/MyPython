#coding:utf-8
import datetime
#test-15:运算符的嵌套使用
def test5():
    score = int(raw_input("输入分数："))

    if score > 90:
        print "good"
    elif score > 60:
        print "middle"
    else:
        print "bad"

#test-16:输出指定日期
def showtime():
    print (datetime.date.today().strftime('%d、%m、%Y'))

#test-17:判断各种符号的个数
def checkstr():
    str = raw_input("输入一行字符窜")
    al = 0  #字母
    sp = 0  #空格
    di = 0  #数字
    ot = 0  #其他
    for c in str:
        if c.isalpha():
            al +=1
        elif c.isdigit():
            di +=1
        elif c.isspace():
            sp +=1
        else:
            ot +=1
    print al,sp,di,ot

#test-18 :求叠数相加的值
def addnum():
    n = int(raw_input("个数"))
    s = int(raw_input("数字"))
    tn = s
    List = []
    for i in range(n):
        List.append(tn)
        tn = 10*tn+s
    print List
    print sum(List)

#test-19:寻找完数
def shownum():
     for i in range(1,1000):
        List = []
        for j in range(1,int(i/2)+1):
            if (i%j == 0):
                List.append(j)
        if sum(List)==i:
            print i
            print List
#shownum()
#addnum()
#checkstr()
#showtime()
#test5()