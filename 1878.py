class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        def judge(p):
            x,y = p
            return  x in range(m) and y in range(n)
        m = len(grid)
        n = len(grid[0])
        ans=[]
        for i in range(m):
            for j in range(n):
                ans.append(grid[i][j])
                for k in range(1,max(m,n)//2+1):
                    p1 = (i,j)
                    p2 = (i+k,j-k)
                    p3 = (i+2*k,j)
                    p4 = (i+k,j+k)
                    if judge(p1) and judge(p2) and judge(p3) and judge(p4):
                        tot = grid[p1[0]][p1[1]]+grid[p2[0]][p2[1]]+grid[p3[0]][p3[1]]+grid[p4[0]][p4[1]]
                        for l in range(1,k):
                            tot += grid[i+l][j-l]+grid[i+l][j+l]+grid[i+2*k-l][j-l]+grid[i+2*k-l][j+l]
                        ans.append(tot)
                    else:
                        break
        ans = list(set(ans))
        ans.sort(reverse = True)
        if len(ans)<=3:
            return ans
        else:
            return ans[:3]
a = Solution()
print(a.getBiggestThree([[20,17,9,13,5,2,9,1,5],[14,9,9,9,16,18,3,4,12],[18,15,10,20,19,20,15,12,11],[19,16,19,18,8,13,15,14,11],[4,19,5,2,19,17,7,2,2]]))
