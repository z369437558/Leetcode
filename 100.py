class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import operator
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            if q is None:
                return True
            else:
                return False
        if q is None:
            if p is None:
                return True
            else:
                return False
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        self.firstsearch(p,list1)
        self.firstsearch(q,list2)
        self.midsearch(p,list3)
        self.midsearch(q,list4)
        if operator.eq(list1,list2)==True and operator.eq(list3,list4)==True:
            return True
        else:
            return False
    def firstsearch(self,now,list1):
        list1.append(now.val)
        if now.left is not None:
            self.firstsearch(now.left,list1)
        if now.right is not None:
            self.firstsearch(now.right,list1)
    def midsearch(self,now,list1):
        
        if now.left is not None:
            self.midsearch(now.left,list1)
        list1.append(now.val)
        if now.right is not None:
            self.midsearch(now.right,list1)
ans = Solution()
p=TreeNode(1)
p.left=TreeNode(2)
# p.right=TreeNode(3)
q=TreeNode(1)
# q.left=TreeNode(2)
q.right=TreeNode(2)
print(ans.isSameTree(p,q))