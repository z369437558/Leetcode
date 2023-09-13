def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ans=""
    p=0
    for i in range(len(strs)):
        if len(strs[i])==0:
            return ""
    while True:

        for i in range(len(strs)-1):
            if len(strs[i])==0:
                    return ans
            if p >= len(strs[i]):
                return ans
            if strs[i][p]!=strs[i+1][p]:
                return ans
        ans = ans + strs[0][p]
        p=p+1
strs = ["a"]
print(longestCommonPrefix(strs))