class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=senate.count('R')
        d=senate.count('D')
        while r>=1 and d>=1:
            decd=0
            decr=0
            s=''
            for i in range(len(senate)):
                if senate[i]=='R':
                    if decr==0:
                        decd+=1
                        s+='R'
                    else:
                        decr-=1
                if senate[i]=='D':
                    if decd==0:
                        decr+=1
                        s+='D'
                    else:
                        decd-=1
            p=0
            senate=s
            decd=min(decd,senate.count('D'))
            decr=min(decr,senate.count('R'))
            if decd>0 or decr>0:
                s=''
            while p<len(senate):
                if senate[p]=='R':
                    if decr>0:
                        decr-=1
                    else:
                        s+='R'
                if senate[p]=='D':
                    if decd>0:
                        decd-=1
                    else:
                        s+='D'
                p+=1
            senate=s
            r=senate.count('R')
            d=senate.count('D')
        if r==0:
            return 'Dire'
        else:
            return 'Radiant'
a = Solution()
a.predictPartyVictory("RRDDD")