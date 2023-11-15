from collections import Counter
class Solution:
    def findSubstring(self, s: str, words):
        ans = []
        c = [{} for i in range(len(words[0]))]
        C =Counter(words)
        for j in range(len(words[0])):
            list1 = [s[j+i*len(words[0]):j+i*len(words[0])+len(words[0])] for i in range(len(words))]
            c[j]= Counter(list1)
            if c[j]==C:
                ans.append(j)
        for i in range(len(words[0]),len(s)-len(words)*len(words[0])+1):
            preword = s[i-len(words[0]):i]
            nextword = s[i+(len(words)-1)*len(words[0]):i+(len(words))*len(words[0])]
            c[i%(len(words[0]))][preword]-=1
            if nextword in c[i%(len(words[0]))]:
                c[i%(len(words[0]))][nextword]+=1
            else:
                c[i%(len(words[0]))][nextword]=1
            if C==c[i%(len(words[0]))]:
                ans.append(i)
        return ans
a = Solution()
print(a.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))