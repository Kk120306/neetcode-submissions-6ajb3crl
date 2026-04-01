# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dsf(root, depth):
            if not root:
                return
            
            if depth == len(res):
                res.append([root.val])
            else:
                res[depth].append(root.val)
            
            dsf(root.left, depth + 1)
            dsf(root.right, depth + 1)
        
        dsf(root, 0)
        return res