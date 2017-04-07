# -*- coding: UTF-8 -*-
def isNumber(num):
    temp=num
    result=[]
    while(temp/10!=0):
        result.append(temp%10)
        temp=temp/10
    result.append(temp)
    sum=0
    for n in result:
        sum=sum+n**3
    if sum==num:
        return True
    return False

results=[]
resultSum=0
for i in range(100,1000):
    if isNumber(i):
        results.append(i)
        resultSum=resultSum+i
for index,num in enumerate(results):
    print "第%d个水仙花数：%d" %(index,num)
print "水仙花数总和为：%d" %(resultSum)