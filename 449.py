
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        """
        self.list1=[]
        if root==None:
            return ""
        def f(root):
            if root is None:
                return
            
            if root.left is not None:
                f(root.left)
            if root.right is not None:
                f(root.right)
            self.list1.append(str(root.val))
        f(root)
        return ",".join(self.list1)
        
    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        if data=="":
            return None
        list2 = data.split(',')
        def f1(left,right):

            root=TreeNode(int(list2[right]))
            if left==right:
                return root
            for i in range(left,right+1):
                if int(list2[i])>=int(list2[right]):
                    if i>=1:
                        root.left = f1(left,i-1)
                        
                    if i!=right:
                        root.right= f1(i,right-1)
                        
                    
                    return root
        return f1(0,len(list2)-1)
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
root = TreeNode(None)
llist=[2,1,3]
root=listCreatTree(root,llist,0)
a=Codec()
s = a.serialize(root)
a.deserialize(s)