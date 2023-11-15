class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=numRows
        if n==1:
            return s
        q=[[]for i in range(n)]
        q[0].append(0)
        q[n-1].append(n-1)
        gap=2*n-2
        ans=''
        for i in range(1,n-1):
            q[i].append(i)
            q[i].append(2*n-2-i)
        for i in range(n):
            while q[i]:
                index = q[i][0]
                del q[i][0]
                if index<len(s):
                    ans+=s[index]
                if index+gap <len(s):
                    q[i].append(index+gap)
        return ans
a = Solution()
print(a.convert(s = "PAYPALISHIRING", numRows = 4))