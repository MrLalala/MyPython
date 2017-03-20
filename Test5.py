#coding:utf-8
#判断三个整数的大小,并输出
List = []
List.append(int(raw_input("第一个数")))
List.append(int(raw_input("第二个数")))
List.append(int(raw_input("第三个数")))

for x in range(0,2):
    for y in range(1,3-x):
        if List[y]<List[y-1]:
            temp = List[y]
            List[y] = List[y-1]
            List[y-1]=temp
print List

#感觉没必要用冒泡排序
