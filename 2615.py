class Solution:
    def distance(self, nums) :
        def dis(index,d):
            n=len(d)
            tot=0
            for i in range(index):
                tot+=(i+1)*d[i]
            for i in range(index,len(d)):
                tot+=(len(d)-i)*d[i]
            return tot
        index=[i for i in range(len(nums))]
        nums, index = zip(*sorted(zip(nums, index)))
        d=[]
        left=0
        ans=[0 for i in range(len(nums))]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                d.append(index[i]-index[i-1])
            else:
                for j in range(left,i):
                    ans[index[j]]=dis(j-left,d)
                d=[]
                left=i
        for j in range(left,len(nums)):
            ans[index[j]]=dis(j-left,d)
        return ans
a = Solution()
a.distance([3,3,0,2])