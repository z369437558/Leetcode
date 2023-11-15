class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        tot=1
        list1=[]
        ans=0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                list1.append(tot)
                tot=1
            else:
                tot+=1
        list1.append(tot)
        for i in range(1,len(list1)):
            ans+=min(list1[i],list1[i-1])
        return ans
a= Solution()
print(a.countBinarySubstrings("00110011"))