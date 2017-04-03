dates=raw_input().split(" ")
tests=int(dates[0])
cases=[]
case=[]
count=0
for  index,date in enumerate(dates):
    if  index==0:
        counts = int(dates[0])

    else:
        case.append(date)
        if index%5==0 and case is not[]:
            cases.append(case)
            case=[]
        # count=1+count

print(cases)