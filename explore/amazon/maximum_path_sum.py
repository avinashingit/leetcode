# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        def maxgain(root):
            nonlocal maxsum
            if not root:
                return 0

            left = max(maxgain(root.left), 0)
            right = max(maxgain(root.right), 0)

            maxsum = max(maxsum, left + right + root.val)

            return root.val + max(left, right)
        maxsum = float("-inf")
        maxgain(root)
        return maxsum
