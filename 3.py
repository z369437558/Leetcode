class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p=0
        ans=0
        flag={}
        start=0
        end=0
        while end<len(s):
            if s[end] not in flag:
                flag[s[end]]=end
            else:
                ans=max(ans,end-start)
                start = max(flag[s[end]]+1,start)
                flag[s[end]]=end
            end+=1
        ans=max(ans,end-start)
        return ans
a = Solution()
print(a.lengthOfLongestSubstring("abba"))