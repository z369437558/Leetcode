from collections import Counter 
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        tot=0
        change=[]
        c=Counter(s) 
        if s==goal and c.most_common(1)[1][1]>=2:
            return True
        for i in range(len(s)):
            if s[i]!=goal:
                tot+=1
                change.append(i)
        if tot!=2:
            return False
        if s[change[0]]==goal[change[1]] and s[change[1]]==goal[change[0]]:
            return True
        return False
a=Solution()
a.buddyStrings("aaaaaaabc","aaaaaaacb")