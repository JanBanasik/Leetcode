# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    max_product = 0
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9 + 7
        total_sum = self._compute_total_sum(root)
        max_sum = self._find_max_sum(root, total_sum)
        return self.max_product % mod
        

    def _compute_total_sum(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return node.val
        return node.val + self._compute_total_sum(node.left) + self._compute_total_sum(node.right)


    def _find_max_sum(self, root, total_sum):
        if not root:
            return 0
        left_sum = self._find_max_sum(root.left, total_sum)
        right_sum = self._find_max_sum(root.right, total_sum)
        current_sum = root.val + left_sum + right_sum
        product = current_sum * (total_sum - current_sum)
        self.max_product = max(self.max_product, product)
        return current_sum
