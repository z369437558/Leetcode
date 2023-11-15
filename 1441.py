class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        p=1
        ans=[]
        for i in range(len(target)):
            while  target[i]!=p:
                p+=1
                ans.append('Push')
                ans.append('Pop')
            ans.append('Push')
            p+=1
        return ans
a = Solution()
print(a.buildArray([1,3],3))