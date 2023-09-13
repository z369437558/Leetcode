class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        ans = 0
        if k==0:
            if num%10==0:
                return 1
            else:
                return -1
        for i in range(10):
            if i*k% 10 == num%10:
                for j in range(int(num/k)+1):
                    if (num-j*k)%10 ==0:
                        ans = j
                        return j
        if ans != 0 :
            return ans
        else:
            return -1
a = Solution()
a.minimumNumbers(num = 10, k = 8)