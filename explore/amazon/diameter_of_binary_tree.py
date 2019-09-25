# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def check(root):
            nonlocal diameter
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            diameter = max(diameter, left + right + 1)
            return max(left, right) + 1
        diameter = 1
        check(root)
        return diameter-1
