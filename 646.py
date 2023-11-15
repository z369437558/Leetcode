class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        ans=[]
        pairs.sort(key = lambda x:x[0])
        def caninput(pair):
            return  ans==[] or pair[0]>ans[-1][1]
        for i in range(len(pairs)):
            if caninput(pairs[i]):
                ans.append(pairs[i])
            else:
                if pairs[i][1]<ans[-1][1]:
                    ans[-1]=pairs[i]
        return len(ans)
a = Solution()
a.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]])