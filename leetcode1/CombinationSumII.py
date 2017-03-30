class Solution(object):
    def sum(self,l):
        sum=0
        for num in l:
            sum=sum+num
        return sum
    def combinationSum2(self, candidates, target):
         """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results=[]
        for num in candidates:
            if target==0:
                break
            sec=target-num
            if sec<0:
                continue
            if sec==0:
                result=[]
                result.append(target)
                results.append(result)
            elif sec in candidates:
                result = [target - sec]
                result.append(target-num)
                results.append(result)
            temp=candidates[:]
            temp.pop(temp.index(num))
            if len(temp)==0:
                break
            preResults=self.combinationSum2(temp, sec)
            for preResult in preResults:
                preResult.append(num)
            results=results+preResults
        finRes=[]
        for result in results:
            if sum(result)==target and len(result)!=0:
                finRes.append(result.sort())
        print(finRes)
        return results
s=Solution()
# can=[10, 1, 2, 7, 6, 1, 5]
can=[1,1,5,4]
tar=8
print(s.combinationSum2(can,tar))