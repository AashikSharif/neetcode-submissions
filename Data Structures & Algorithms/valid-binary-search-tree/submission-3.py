# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValid(root,left,right):
            if not root:
                return True
            elif (left<root.val<right):
                lbin=rbin=True
                if root.left:
                    lbin = checkValid(root.left,left,root.val)
                if root.right:
                    rbin = checkValid(root.right,root.val,right)
                return lbin and rbin
            return False

        return checkValid(root, -1100,1100)