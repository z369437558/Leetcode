from collections import Counter
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        c = Counter(candidates)
        candidates=list(set(candidates))
        candidates.sort()
        def dfs(t,index,path):

            if t==0:
                ans.append(path)
                return
            if t<0:
                return 
            for i in range(index,len(candidates)):
                if path.count(candidates[i])<c[candidates[i]]:
                    dfs(t-candidates[i],i,path+(candidates[i],))

        dfs(target,0,())
        return ans
a = Solution()
print(a.combinationSum2(candidates = [1,2,7,6,1,5], target = 8))