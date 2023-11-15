class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]):
        def creatBST(nums):
            if nums==[]:
                return None
            root = TreeNode(nums[len(nums)//2])
            root.left = creatBST(nums[:len(nums)//2])
            root.right = creatBST(nums[len(nums)//2+1:])
            return root
        return creatBST(nums)
a = Solution()
a.sortedArrayToBST(nums=[-10,-3,0,5,9])