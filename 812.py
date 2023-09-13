class Solution:
    def largestTriangleArea(self, points) -> float:
        ans=0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]
                    ans = max(ans, 0.5 * abs((p1[0]*p2[1] - p2[0]*p1[1]) + (p2[0]*p3[1] - p3[0]*p2[1]) + (p3[0]*p1[1] - p1[0]*p3[1])))
        return ans
a =Solution()
a.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])