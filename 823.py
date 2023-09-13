class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        f={i:1 for i in arr}
        arr.sort()
        set1 = set(arr)
        for i in range(len(arr)):
            for j in range(i):
                if arr[i]%arr[j]==0 and arr[i]//arr[j] in set1:
                        f[arr[i]]+=(f[arr[j]]*f[arr[i]//arr[j]])
        return sum(f)
a = Solution()
a.numFactoredBinaryTrees([2,4,5,10])