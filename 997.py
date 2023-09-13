from collections import Counter
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        list1 = [trust[i][1] for i in range(len(trust)) ]
        c= Counter(list1)
        if len(trust)==0:
            if n==1:
                return 1
            else:
                return -1
        ans = int (c.most_common(1)[0][0])
        for i in range(len(trust)):
            if trust[i][0]==ans:
                return -1
        if c[ans]==n-1:
            return ans
        return -1
a=Solution()
a.findJudge(n = 4, trust = [[1,3],[1,4],[2,3]])