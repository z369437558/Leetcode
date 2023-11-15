class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans=[]
        for i  in range(40):
            for j in range(20):
                for k in range(15):
                    ans.append(1*2**i*3**j*5**k)
        ans.sort()
        return ans[n-1]
a = Solution()
a.nthUglyNumber(1000)