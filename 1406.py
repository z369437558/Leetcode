class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        def check():
            if dp[0]>sum(stoneValue)-dp[0]:
                return 'Alice'
            if dp[0]==sum(stoneValue)-dp[0]:
                return 'Tie'
            if dp[0]<sum(stoneValue)-dp[0]:
                return 'Bob'
        dp = [-5*10**7 for i in range(len(stoneValue)+1)]
        dp[-1]=0
        dp[-2] = stoneValue[-1]
        tot = sum(stoneValue)
        if len(dp)==1:
            return check()
        sum1 = [0 for i in range(len(stoneValue))]
        sum1.append(0)
        for i in range(len(stoneValue)):
            tot-=stoneValue[i]
            sum1[i]=tot
        for i in range(len(stoneValue)-2,-1,-1):
            for j in range(1,4):
                if i+j<=len(stoneValue):
                    dp[i]=max(dp[i],sum1[i]-sum1[i+j]+sum1[i+j]-dp[i+j])
        return check()
a = Solution()
print(a.stoneGameIII([1,2,3,6]))