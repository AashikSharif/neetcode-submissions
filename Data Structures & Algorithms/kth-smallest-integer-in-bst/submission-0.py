# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def Traverse(root,k,arr):
            if not root:
                return None
            left = Traverse(root.left,k,arr)
            arr.append(root.val)
            print(arr)
            if(len(arr)==k):
                return arr[k-1]
            
            right = Traverse(root.right,k,arr)

            if left == right == None:
                return None
            elif left == None:
                return right
            elif right == None:
                return left
    
        return Traverse(root,k,arr)
            