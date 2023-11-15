class Solution:
    def maxPoints(self, points) -> int:
        m= len(points)
        n = len(points[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0]=points[0]
        for N in range(1,m):
            for i in range(n):
                for j in range(n):
                    dp[N][i]=max(dp[N][i],dp[N-1][j]+points[N][i]-abs(i-j))
        return max(dp[-1])
a = Solution()
print(a.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))