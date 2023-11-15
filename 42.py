class Solution:
    def trap(self, height: list[int]) -> int:
        stack = [(0,0)]
        height.insert(0,0)
        nowheight=0
        ans=0
        for i in range(1,len(height)):
            if height[i]<stack[-1][0]:
                nowheight=0
            while stack and height[i]>=stack[-1][0] :
                ans+=(i-stack[-1][1]-1)*(stack[-1][0]-nowheight)
                nowheight=stack[-1][0]
                stack.pop()
            if stack:
                ans+=(i-stack[-1][1]-1)*(height[i]-nowheight)
            stack.append((height[i],i))
        return ans
a = Solution()
print(a.trap([4,2,0,3,2,5]))