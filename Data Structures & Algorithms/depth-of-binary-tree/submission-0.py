# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return self.maxdepth(root,1)
        else:
            return 0

    def maxdepth(self,root,n):
        a=b=n
        if root.left: 
            a = self.maxdepth(root.left,a+1)
        if root.right:
            b = self.maxdepth(root.right,b+1)
        
        return max(a,b)