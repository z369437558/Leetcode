class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if num.count(str(i))!=num[i]:
                return False
        return True
a =Solution()
a.digitCount('1210')