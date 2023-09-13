n=10001
ans=[]
for i in range(n):
    s= list(str(i))
    s = list(map(lambda x:int(x),s))
    if len(s)%2==0:
        m=len(s)//2
        if sum(s[:m])==sum(s[m:]):
            ans.append(i)
print(ans)
    