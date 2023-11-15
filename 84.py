class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.insert(0,0)
        heights.append(0)
        stack = [(0,0)]
        ans = 0
        for i in range(1,len(heights)):
            if heights[i]>=stack[-1][0]:
                stack.append((heights[i],i))
            else:
                while heights[i]<stack[-1][0]:
                    ans = max(stack[-1][0]*(i-stack[-2][1]-1),ans)
                    stack.pop()
                stack.append((heights[i],i))
        return ans
                
a = Solution()
print(a.largestRectangleArea([2,1,5,6,2,3]))