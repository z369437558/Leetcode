class Solution:
    def isPathCrossing(self, path: str) -> bool:
        set1 = set()
        set1.add((0,0))
        now=[0,0]
        for i in path:
            if i=="N":
                now[1]+=1
            if i=='S':
                now[1]-=1
            if i=='E':
                now[0]+=1
            if i=='W':
                now[0]-=1
            if (now[0],now[1]) in set1:
                return True
            set1.add((now[0],now[1]) )
        return False
a = Solution()
a.isPathCrossing("NESWW")