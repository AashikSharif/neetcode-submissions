# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        self.traversal(root, 1, arr)     
        return arr

    def traversal(self, root, depth, arr):
        if not root:
            return arr
        else:
            if(len(arr)==depth-1):
                arr.append([])
            
            arr[depth-1].append(root.val)
            self.traversal(root.left,depth+1,arr)
            self.traversal(root.right,depth+1,arr)

        
