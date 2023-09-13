class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        coordinates.sort()
        a= coordinates[1][1]-coordinates[0][1]
        b = coordinates[1][0] - coordinates[0][0]
        if b==0:
            for i in range(len(coordinates)):
                if coordinates[i][0] - coordinates[i-1][0]!=0:
                    return False
            return True
        else:
            k=a/b
            for i in range(len(coordinates)):
                if coordinates[i][0] - coordinates[i-1][0]==0:
                        return False
                else:
                    k1=(coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0] - coordinates[i-1][0])
                if k1!=k:
                    return False
            return True
aa = Solution()
print(aa.checkStraightLine([[0,0],[0,1],[0,-1]]))