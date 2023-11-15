class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def bfs(tot,index):
            if len(list1)==tot:
                ans.add(tuple(sorted(list1.copy())))
            else:
                for i in range(index,len(nums)):
                    list1.append(nums[i])
                    bfs(tot,i+1)
                    list1.pop()
        ans=set()
        list1=[]
        for i in range(len(nums)+1):
            bfs(i,0)
        return list(ans)
a = Solution()
print(a.subsetsWithDup([1,2,2]))