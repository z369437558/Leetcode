class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        score1=score
        index = list(map(lambda i :i ,range(len(score))))
        score, index = zip(*sorted(zip(score, index)))
        index = list(index)
        index.reverse()
        score1[index[0]]="Gold Medal"
        score1[index[1]]="Silver Medal"
        score1[index[2]]="Bronze Medal"
        for i in range(3,len(index)):
            score1[index[i]]=str(i+1)
        return score1

a=Solution()
a.findRelativeRanks([5,4,3,2,1])