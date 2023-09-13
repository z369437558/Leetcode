class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        newimg=[[0 for j in range(len(img[0]))] for i in range(len(img))]
        move=[(0,0),(-1,-1),(-1,1),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1)]
        for i in range(len(img)):
            for j in range(len(img[0])):
                tot=0
                t=0
                for k in move:
                    if i+k[0]>=0 and i+k[0]<len(img) and j+k[1]>=0 and j+k[1]<len(img[0]):
                        tot+=img[i+k[0]][j+k[1]]
                        t+=1
                newimg[i][j]=tot//t
        return newimg
a=Solution()
a.imageSmoother([[100,200,100],[200,50,200],[100,200,100]])