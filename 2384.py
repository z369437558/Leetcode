from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        num = list(num)
        a = [0,0,0,0,0,0,0,0,0,0]
        c = Counter(num)
        ans=''
        for key,value in c.items():
            a[int(key)]=value
        for i in range(len(a)-1,-1,-1):
            ans+=str(i)*(a[i]//2)
            a[i]%=2
        flag=0
        for i in range(len(a)-1,-1,-1):
            if a[i]==1:
                ans+=str(i)
                flag=1
                break
        ans+=ans[-1-flag::-1]
        ans = ans.strip('0')
        if ans=='':
            ans = max(num)
        return ans
a = Solution()
print(a.largestPalindromic(num = "6006"))