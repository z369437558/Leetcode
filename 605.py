class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i==0:
                    if flowerbed[i+1]==0:
                        n=n-1
                        flowerbed[i]=1
                else:
                    if i==len(flowerbed)-1:
                        if flowerbed[i-1]==0:
                            n=n-1
                            flowerbed[i]=1
                    else:
                        if(flowerbed[i-1] and flowerbed[i+1]==0):
                            n=n-1
                            flowerbed[i]=1
        if n<=0:
            return True
        return False
a=Solution()
a.canPlaceFlowers([1,0,0,0,1],2)