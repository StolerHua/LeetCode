def isSpecial(n):
    if n==5:
        return 2
    if n==2:
        return 5
    if n==9:
        return 6
    if n==6:
        return 9
    return 0
def add(results,n1,n2,n3=0):
    if n3==0:
        results.append(n1+n2*10)
        results.append(n1*10+n2)
    else:
        results.append(n1 + n2 * 10 + n3 * 100)
        results.append(n2 + n3 * 10 + n1 * 100)
        results.append(n3 + n1 * 10 + n2 * 100)
def pingjie(n1,n2,n3=0):
    results=[]
    add(results,n1,n2,n3)
    if isSpecial(n1)!=0:
        add(results,isSpecial(n1),n2,n3)
    if isSpecial(n2)!=0:
        add(results,n1,isSpecial(n2),n3)
    if isSpecial(n3)!=0:
        add(results,n1,n2,isSpecial(n3))
    if isSpecial(n1)!=0 and isSpecial(n2)!=0:
        add(results,isSpecial(n1),isSpecial(n2),n3)
    if isSpecial(n1)!=0 and isSpecial(n3)!=0:
        add(results,isSpecial(n1),n2,isSpecial(n3))
    if isSpecial(n2) != 0 and isSpecial(n3) != 0:
        add(results, n1, isSpecial(n2), isSpecial(n3))
    return results
def addnum(results,temp):
    for n in temp:
        results.append(n)
def judge(date):
    if len(date)!=3:
        return -1
    for num in date:
        if num <0 or date.count(num)>1 or num>9:
            return -1
def run():
    results = []
    date = list(raw_input().split(','))
    if judge(date)==-1:
        return -1
    try:
        for index,num in enumerate(date):
            date[index]=int(num)
    except ValueError:
        return -1
    N=sorted(date)[-1]
    addnum(results,date)
    addnum(results,pingjie(date[0],date[1]))
    addnum(results,pingjie(date[0],date[2]))
    addnum(results,pingjie(date[1],date[2]))
    addnum(results,pingjie(date[0],date[1],date[2]))
    return sorted(results)[N]

print(run())