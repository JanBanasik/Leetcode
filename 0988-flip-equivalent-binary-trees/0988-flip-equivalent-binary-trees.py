# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if ((val := self.checkRoots(root1, root2)) > -1):
            return bool(val)
        return self.check(root1, root2)

    def checkRoots(self, root1, root2) -> int:
        if root1 is None and root2 is None:
            return 1
        elif (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
            return 0
        if root1.val != root2.val:
            return 0
        return -1
    
    def check(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        children1 = [root1.left.val if root1.left else -1, root1.right.val if root1.right else -1]
        children2 = [root2.left.val if root2.left else -1, root2.right.val if root2.right else -1]
        if sorted(children1) != sorted(children2):
            return False
        else:
            if children1 != children2:
                root1.left, root1.right = root1.right, root1.left
            return self.check(root1.left, root2.left) and self.check(root1.right, root2.right)
        