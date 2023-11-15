class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        def check(list1):
            max1 = list1[0]
            for i in range(1,len(list1)):
                max1 = max1*list1[i]//gcd(max1,list1[i])
            return max1==k
        ans=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if check(nums[i:j+1]):
                    ans+=1
        return ans
a = Solution()
a.subarrayLCM(nums = [3,6,2,7,1], k = 6)