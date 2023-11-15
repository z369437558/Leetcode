from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        @cache
        def bfs(root):
            if root.left and root.right:
                return max(bfs(root.left)[0],bfs(root.right)[0])+1,abs(bfs(root.left)[0]-bfs(root.right)[0])<=1 and bfs(root.left)[1] and bfs(root.right)[1]
            if root.left:
                return bfs(root.left)[0]+1,bfs(root.left)[0]<=1
            if root.right:
                return bfs(root.right)[0]+1,bfs(root.right)[0]<=1
            return 1,True
        if root:
            return bfs(root)[1]
        return True
def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == None:
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root
root=TreeNode()
llist=[3,9,20,None,None,15,7]
root=listCreatTree(root,llist,0)
a = Solution()
print(a.isBalanced(root))