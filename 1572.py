def main(mat):        
    ans=0
    n = len(mat)
    for i in range(n):
        ans = ans+mat[i][i]+mat[i][n-i-1]
        if n-i-1==i:
            ans = ans-mat[i][i]
    return ans
mat = [[1,2,3],
    [4,5,6],
    [7,8,9]]
print(main(mat))