#coding :utf_8
# while True:
#     try:
#         datas=[]
#         (x,y)= (int(x) for x in raw_input().split())
#             # datas.append(x)
#         print(x+y)
#     except EOFError:
#         break
# print(datas)
n=int(raw_input())
dates=raw_input().split()
# dates=[]
# n=int(receive.split(" ")[0])
# date=receive.split(" ")[1]
# if n<len(date):
#     print("INPUT ERROR!")
# print (n)
# dates=filter(lambda x: (int)(x),list(date))
# print(dates)
dates=dates[::-1]
# print(dates)
results=[]
for num in dates:
    if results==[]:
        results.append(num)
    elif num<results[-1]:
        results.append(num)
    else:
        break
resultStr=str()
for date in dates[::-1]:
    if date not in results:
        print (date)
#         resultStr=resultStr+str(date)+' '
# print (resultStr)
