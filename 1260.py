import numpy as np
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        list1=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                list1.append(grid[i][j])    
        ans=list1[-k:]
        ans.extend(list1[:-k])
        x=np.array(ans)
        x=x.reshape((len(grid),len(grid[0])))
        return x
a=Solution()
grid=[[1,2,3],[4,5,6],[7,8,9]]
k=1
a.shiftGrid(grid,k)