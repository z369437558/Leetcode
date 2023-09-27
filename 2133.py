class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        for row in matrix:
            if max(row)==len(matrix) and min(row)==1 and len(set(row))==len(matrix):
                return False
        return True
a = Solution()
a.checkValid([[1,2,3],[3,1,2],[2,3,1]])