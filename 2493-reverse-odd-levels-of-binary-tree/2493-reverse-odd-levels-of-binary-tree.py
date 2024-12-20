# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = []
        self.getLevels(root, temp, 1)
        temp = [temp[i][::-1] if i % 2 == 1 else temp[i] for i in range(len(temp))]
        return self.constructBinaryTree(temp, 0, 0)
    
    def getLevels(self, root, temp, level):
        if root is None:
            return
        if level > len(temp):
            temp.append([])
        temp[level - 1].append(root.val)
        self.getLevels(root.left, temp, level + 1)
        self.getLevels(root.right, temp, level + 1)
    
    def constructBinaryTree(self, temp, level, index):
        if level >= len(temp):
            return None
        root = TreeNode(temp[level][index])
        root.left = self.constructBinaryTree(temp, level + 1, 2 * index)
        root.right = self.constructBinaryTree(temp, level + 1, 2 * index + 1)
        return root
