class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        ans=0
        row = [0 for i in range(m)]
        col = [0 for i in range(n)]
        for i in indices:
            row[i[0]]=row[i[0]]+1
            col[i[1]]=col[i[1]]+1
        for i in range(len(row)):
            for j in range(len(col[0])):
                ans = ans + (row[i]+col[j])%2
        return ans
a = Solution()
a.oddCells(2,3,[[0,1],[1,1]])