# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSums: list[int] = []
        self.getLevelSums(root, levelSums, 1)
        levelSums.sort()
        print(levelSums)
        return levelSums[-k] if k <= len(levelSums) else -1
    
    def getLevelSums(self, root, levelSums, level):
        if root is None:
            return
        if level > len(levelSums):
            levelSums.append(0)
        levelSums[level - 1] += root.val
        self.getLevelSums(root.left, levelSums, level + 1)
        self.getLevelSums(root.right, levelSums, level + 1)