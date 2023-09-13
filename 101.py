def f(ans):
    p=1
    while len(ans)>0:
        if ans[:2**(p-1)]==ans[2**(p-1)-1::-1]:
            ans=ans[2**(p-1):]
            p+=1
        else:
            return False
    return True
print(f([1,2,2,3,4,4,3]))
