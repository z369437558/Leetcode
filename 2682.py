def move(now,dis,flag,n):
    target = (now+dis)%n
    if target == 0:
        target = n
    if  flag[target]==1:
        return -1
    else:
        flag[target]=1
        return target
def main():
    n=5
    k=2
    flag=[0 for i in range(n+1)]
    ans=[]
    now=1
    times=1
    flag[1]=1
    while True:
        now = move(now,k*times%n,flag,n)  
        if now == -1:
            break
        times=times+1
    for i in range(1,len(flag)):
        if flag[i]==0:
            ans.append(i)
    print(ans)
main()
