import numpy as np
import math
class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        set1=set()
        ans=0
        b = [0 for i in range(len(arr))]
        for i in range(k):
            list1 = []
            p=i
            if b[p]==1:
                break
            while b[p]==0:
                list1.append(arr[p])
                b[p]=1
                p+=k
                if p>=len(arr):
                    p=p % len(arr)
            median  =  math.ceil(np.median(list1))
            for x in list1:
                ans+=abs(x-median)
        return ans

a = Solution()
print(a.makeSubKSumEqual(arr = [2,10,9], k = 1))