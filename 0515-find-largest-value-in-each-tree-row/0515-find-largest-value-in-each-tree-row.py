# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result: list[int] = []
        self.getLevelMinimum(root, result, 0)
        return result
    
    def getLevelMinimum(self, root, result, currentLevel):
        if root is None:
            return
        
        if currentLevel == len(result):
            result.append(-float('inf'))
        
        result[currentLevel] = max(result[currentLevel], root.val)
        self.getLevelMinimum(root.left, result, currentLevel + 1)
        self.getLevelMinimum(root.right, result, currentLevel + 1)
