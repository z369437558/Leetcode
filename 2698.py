class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(x):
            def dfs(s,target):
                if len(s)>0:
                    flag = False
                    for i in range(len(s)):
                        list1.append(s[:i+1])
                        flag = flag or dfs(s[i+1:],target)
                        list1.pop()   
                    return flag 
                else:
                    tot=0
                    for c in list1:
                        tot+=int(c)
                    return tot==target
            s = str(x*x)
            list1 = []
            return dfs(s,x)
        ans = 0
        for i in range(1,n+1):
            if check(i):
                ans+=i*i
        return ans
a = Solution()
print(a.punishmentNumber(10))