class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def find(list1):
            l=0
            r = len(list1)-1
            while l<r:
                mid = (l+r)//2+1
                if list1[mid]<=target:
                    l = mid
                else:
                    r = mid-1
            return list1[l]==target

        l = 0
        r = len(matrix)-1
        while l<r:
            mid = (l+r)//2+1
            if matrix[mid][0]<=target:
                l = mid
            else:
                r = mid-1
        if matrix[l][0]!=target:
            maxrow = l
        else:
            return True

        l = 0
        r = len(matrix[0])-1
        while l<r:
            mid = (l+r)//2+1
            if matrix[0][mid]<=target:
                l = mid
            else:
                r = mid-1
        if matrix[0][l]!=target:
            maxcol = l     
        else:
            return True
        for i in range(maxrow+1):
            if find(matrix[i][:maxcol+1]):
                return True
        return False  
a = Solution()
print(a.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))