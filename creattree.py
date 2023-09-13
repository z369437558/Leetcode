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
root=TreeNode()
llist=[1,2,3,4,None,5]
root=listCreatTree(root,llist,0)