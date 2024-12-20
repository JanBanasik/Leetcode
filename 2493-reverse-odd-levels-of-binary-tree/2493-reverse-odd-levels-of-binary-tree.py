# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        self.traverse(root.left, root.right, 0)
        return root
    
    def traverse(self, left, right, level):
        if left is None or right is None:
            return
        
        if level % 2 == 0:
            left.val, right.val = right.val, left.val
        
        self.traverse(left.left, right.right, level + 1)
        self.traverse(left.right, right.left,  level + 1)
