class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans=[]
        for i in range(1,10):
            s=str(i)
            for j in range(9):
                s+=str(int(s[j])+1)
                if int(s) in range(low,high+1):
                    ans.append(int(s))
        return ans
a =Solution()
print(a.sequentialDigits(100,300))