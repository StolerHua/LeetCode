# # # class Solution(object):
# # #     def order(self,key1,key2,dic):
# # #         return dic[key1]<=dic[key2]
# # #     def maxProfit(self, prices):
# # #         """
# # #         :type prices: List[int]
# # #         :rtype: int
# # #         """
# # #         i=0
# # #         index=[]
# # #         length=len(prices)
# # #         while(i<length):
# # #             index.append(i)
# # #             i=i+1
# # #         dic=dict(zip(prices, index))
# # #         # for price in dic:
# # #         #     print(dic[price])
# # #         temp=sorted(prices)
# # #         # print(temp)
# # #         p=0;
# # #         q=length-1;
# # #         while p<q:
# # #             if self.order(temp[p],temp[q],dic):
# # #                 return temp[q]-temp[p]
# # #             elif self.order(temp[p+1],temp[q],dic) and temp[q]-temp[p+1]>temp[q-1]-temp[p] :
# # #                 return  temp[q]-temp[p+1]
# # #             elif self.order(temp[p],temp[q-1],dic) and temp[q]-temp[p+1]<temp[q-1]-temp[p] :
# # #                 return temp[q-1] - temp[p]
# # #             elif p+1>q-1 and temp[q]-temp[p+1]>temp[q-1]-temp[p] and self.order(temp[p+1],temp[q],dic)==False:
# # #                 return temp[q-1] - temp[p]
# # #             elif p+1>q-1 and temp[q]-temp[p+1]<temp[q-1]-temp[p] and self.order(temp[p],temp[q-1],dic)==False:
# # #                 return temp[q] - temp[p + 1]
# # #             p=p+1
# # #             q=q-1
# # #         return 0
# # #
# # class Solution(object):
# #     def order(self,key1,key2,dic):
# #         return dic[key1]<=dic[key2]
# #     def compare(self,p,q,temp):
# #         return int(temp[q]-temp[p+1])>int(temp[q-1]-temp[p])
# #     def deleteSame(self,temp):
# #         for num in temp:
# #             while temp.count(num)>1:
# #                 temp[temp.index(num)]=num+temp.count(num)*0.01
# #         return temp
# #     def maxProfit(self, prices):
# #         """
# #         :type prices: List[int]
# #         :rtype: int
# #         """
# #         i=0
# #         index=[]
# #         length=len(prices)
# #         while(i<length):
# #             index.append(i)
# #             i=i+1
# #         dic=dict(zip(self.deleteSame(prices), index))
# #         temp=sorted(prices)
# #         p=0;
# #         q=length-1;
# #         countp = countq = 0
# #         while p<q:
# #             if self.order(temp[p],temp[q],dic):
# #                 return int(round(temp[q]-temp[p]))
# #             elif self.order(temp[p+1],temp[q],dic) and self.compare(p,q,temp):
# #                 return int(round(temp[q]-temp[p+1]))
# #             elif self.order(temp[p],temp[q-1],dic) and self.compare(p,q,temp)==False :
# #                 return int(round(temp[q-1] - temp[p]))
# #             elif self.order(temp[p+1],temp[q],dic) and temp[q]-temp[p+1]>0:
# #                 return int(round(temp[q]-temp[p+1]))
# #             elif self.order(temp[p],temp[q-1],dic) and temp[q-1] - temp[p]>0:
# #                 return int(round(temp[q-1] - temp[p]))
# #
# #             if int(temp[p+1]-temp[p])==0 and countp!=1:
# #                 countp=1
# #                 p=p+1
# #                 continue
# #             elif int(temp[q]-temp[q-1])==0 and countq!=1:
# #                 countq=1
# #                 q=q-1
# #                 continue
# #             else:
# #                 p=p+1
# #                 q=q-1
# #                 countp = countq = 0
# #         return 0
# #
#
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         results=[]
#         result=[]
#         for price in prices:
#             if result==[]:
#                 result.append(price)
#             elif result[-1]<=price:
#                 result.append(price)
#             else:
#                 results.append(result)
#                 result=list()
#                 result.append(price)
#             for re in results:
#                 if re[-1]<price:
#                     re.append(price)
#         # if results==[]:
#         results.append(result)
#         max=0
#         if result==[]:
#             return 0
#         for result in results:
#             if result[-1]-result[0]>max:
#                 max=result[-1]-result[0]
#         return max
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        results=[]
        profit=[]
        if len(prices)==0 or len(prices)==1:
            profit.append(0)
        for price in prices:
            if results == []:
                results.append(price)
            elif results[-1]>=price:
                results.pop()
                results.append(price)
                profit.append(results[-1] - results[0])
            else:
                results.append(price)
                profit.append(results[-1] - results[0])
                results.pop()
        return sorted(profit)[-1]
# prices=[2,1,2,1,0,1,2]
prices=[1]
# prices=[7, 1, 5, 3, 6, 4]
# prices=[1,2,4,2,5,7,2,4,9,0,9]
s=Solution()
print(s.maxProfit(prices))