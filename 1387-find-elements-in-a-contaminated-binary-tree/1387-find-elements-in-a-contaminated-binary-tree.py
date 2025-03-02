# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values
    
    def recover(self, root, value):
        result = TreeNode(value)
        self.values.add(value)
        if root.left:
            result.left = self.recover(root.left, 2 * value + 1)
        if root.right:
            result.right = self.recover(root.right, 2 * value + 2)
        return result



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)