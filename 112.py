class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'列表创建二叉树'


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
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        ans=[False]
        self.search(root,targetSum,ans)
        return ans[0]
    def search(self,now,targetSum,ans):
        if now.val == targetSum and now.left is None and now.right is None:
            ans[0]=True
        if now.left is not None:
            now.left.val = now.val+now.left.val
            self.search(now.left,targetSum,ans)
        if now.right is not None:
            now.right.val = now.val+now.right.val
            self.search(now.right,targetSum,ans)

if __name__ == '__main__':
    llist = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = listCreatTree(None, llist, 0)
    targetSum=22
    a = Solution()
    print(a.hasPathSum(root,targetSum))

