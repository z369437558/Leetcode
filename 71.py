class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for i in range(len(path)):
            if path[i]=='/':
                while stack and stack[-1]=='/':
                    stack.pop()
            stack.append(path[i])
        s= ''.join(stack)
        s=s.split('/')
        stack=[]    
        for i in range(len(s)):
            if s[i]=='.':
                pass
            elif s[i]=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        ans = '/'.join(stack)
        if len(ans)>1 and ans[-1]=='/':
            ans=ans[:-1]
        if ans=='':
            return '/'
        return ans 
a = Solution()
a.simplifyPath(path = "/home//foo/")