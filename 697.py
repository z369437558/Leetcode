class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        # def f(list1):
        #     for i in range
        # def fun(list1,mid,n):
        #     for i in range(len(list1)-mid+1):
        #         if f(list1[i:i+mid])==n:
        #             return True
        #     return False
        # n= f(nums)
        # left=n
        # right=len(nums)
        # while left<right:
        #     mid =(left+right)//2
        #     if fun(nums,mid,n):
        #         right= mid
        #     else:
        #         left=mid+1
        # return left 
        max1=0
        tot=[0 for i in range(50001)]
        first = [0 for i in range(50001)]
        last = [0 for i in range(500001)]
        for i in range(len(nums)):
            if tot[nums[i]]==0:
                first[nums[i]]=i
            last[nums[i]]=i
            tot[nums[i]]+=1
            if tot[nums[i]]>max1:
                max1 = tot[nums[i]]
                most =set()
                most.add(nums[i])
            elif tot[nums[i]]==max1:
                most.add(nums[i])
        min1 = 50000
        for num in most:
            min1 = min(last[num]-first[num]+1,min1)
        return min1
a = Solution()
a.findShortestSubArray([1,2,2,3,1,4,2])