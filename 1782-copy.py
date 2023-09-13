class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        count1,count2=[0]*n,Counter()
        for e in edges:
            count1[e[0]-1]+=1
            count1[e[1]-1]+=1
            a=20005*(max(e[0],e[1])-1)+min(e[0],e[1])-1
            count2[a]+=1
        copy=sorted(count1)
        for i in range(len(queries)):
            a,s,l,r=queries[i],0,0,n-1
            while l<n:
                while r>=0 and copy[l]+copy[r]>a:
                    r-=1
                s+=n-max(l,r)-1
                l+=1
            for b in count2:
                c,u,v=count2[b],b//20005,b%20005
                if count1[u]+count1[v]>a and count1[u]+count1[v]-c<=a:
                    s-=1
            queries[i]=s
        return queries
a=Solution()
a.countPairs(6,[[5,2],[3,5],[4,5],[1,5],[1,4],[3,5],[2,6],[6,4],[5,6],[4,6],[6,2],[2,6],[5,4],[6,1],[6,1],[2,5],[1,3],[1,3],[4,5]],[6,9,2,1,2,3,6,6,6,5,9,7,0,4,5,9,1,18,8,9])