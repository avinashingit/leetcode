# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def check(self, root, min_val, max_val):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.check(root.left, min_val, root.val) and self.check(root.right, root.val, max_val)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root, float("-inf"), float("inf"))
