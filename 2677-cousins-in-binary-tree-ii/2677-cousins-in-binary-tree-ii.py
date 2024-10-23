# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        copiedRoot = root
        levelSums = []
        self.findLevelSums(root, 1, levelSums)
        return self.getTree(root, 1, levelSums, 0)

    def getTree(self, root, depth, levelSums, value):
        if root is None:
            return TreeNode()

        result = TreeNode(value)
        l = root.left.val if root.left else 0
        r = root.right.val if root.right else 0
        if root.left:
            result.left = self.getTree(root.left, depth + 1, levelSums, levelSums[depth] - l - r)
        if root.right:
            result.right = self.getTree(root.right, depth + 1, levelSums, levelSums[depth] - l - r)
        return result
    def findLevelSums(self, root, depth, levelSums):
        if root is None:
            return
        if depth > len(levelSums):
            levelSums.append(0)
        levelSums[depth - 1] += root.val

        self.findLevelSums(root.left, depth + 1, levelSums)
        self.findLevelSums(root.right, depth + 1, levelSums)