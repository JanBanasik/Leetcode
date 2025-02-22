# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    index = 0
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        roots = []
        dashes = 0
        number = ""
        for val in traversal:
            if val == '-':
                if not number:
                    dashes +=1
                else:
                    roots.append((dashes, int(number)))
                    dashes = 1
                    number = ""
            else:
                number += val
        roots.append((dashes, int(number)))
        
        return self.createTree(roots)
    
    def createTree(self, roots):
        root = TreeNode(roots[self.index][1])
        currDashes = roots[self.index][0]
        self.index +=1

        if self.index == len(roots):
            return root

        if roots[self.index][0] == roots[self.index - 1][0] + 1:
            root.left = self.createTree(roots)
        
        if self.index < len(roots):
            if currDashes + 1== roots[self.index][0]:
                root.right = self.createTree(roots)

        return root
