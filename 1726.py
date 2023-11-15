class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        ans=0
        # set1 = set(nums)
        chengji = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]*nums[j] in chengji:
                    chengji[nums[i]*nums[j]]+=1
                else:
                    chengji[nums[i]*nums[j]]=1
        for k,v in chengji.items():
            if v>=2:
                ans+=v*(v-1)//2*8
        return ans
a = Solution()
print(a.tupleSameProduct([20,10,6,24,15,5,4,30]))