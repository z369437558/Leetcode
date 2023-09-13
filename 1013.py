class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:
        tot =sum(arr)
        if tot%3!=0:
            return False
        t=0
        left=-1
        for i in range(len(arr)):
            t+=arr[i]
            if t==tot//3:
                left=i
                break
        if left==-1:
            return False
        t=0
        right=-1
        for i in range(left+1,len(arr)):
            t+=arr[i]
            if t==tot//3:
                right=i
                break
        if right==-1:
            return False
        if left>=1 and right<=len(arr)-2:
            return True
        return False
a=Solution()
a.canThreePartsEqualSum([0,0,0,0])