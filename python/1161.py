# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:

    def dfs(self, root, level_values, level):
        if root is None:
            return
        level_values[level] += root.val
        self.dfs(root.left, level_values, level+1)
        self.dfs(root.right, level_values, level+1)

    def maxLevelSum(self, root: TreeNode) -> int:
        level_values = defaultdict(int)
        self.dfs(root, level_values, 1)
        return max(level_values, key=level_values.get)
