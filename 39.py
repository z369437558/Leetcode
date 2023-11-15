class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        def dfs(t,index,path):
            if t==0:
                ans.append(path)
                return
            if t<0:
                return 
            for i in range(index,len(candidates)):
                dfs(t-candidates[i],i,path+(candidates[i],))
        dfs(target,0,())
        return ans
a = Solution()
print(a.combinationSum(candidates = [2,3,6,7], target = 7))