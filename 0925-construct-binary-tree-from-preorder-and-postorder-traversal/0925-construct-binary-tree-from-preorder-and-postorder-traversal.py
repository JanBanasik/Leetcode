# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        numOfNodes = len(preorder)
        return self._constructTree(0, numOfNodes - 1, 0, preorder, postorder)
    
    def _constructTree(
        self,
        pre_start: int,
        pre_end: int,
        post_start: int,
        preorder: List[int],
        postorder: List[int]
    ) -> Optional[TreeNode]:
        
        if pre_start > pre_end:
            return None
        
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])
        
        numLeftNodes = 1
        left_root = preorder[pre_start + 1]
        while postorder[post_start + numLeftNodes - 1] != left_root:
            numLeftNodes +=1
        
        root = TreeNode(preorder[pre_start])

        root.left = self._constructTree(
            pre_start + 1,
            pre_start + numLeftNodes,
            post_start,
            preorder,
            postorder
        )
        root.right = self._constructTree(
            pre_start + numLeftNodes + 1,
            pre_end,
            post_start + numLeftNodes,
            preorder,
            postorder
        )
        return root


