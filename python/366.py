# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict


class Solution:

    def dfs(self, root, l):
        if root is None:
            return None
        if root.left is None and root.right is None:
            l.append(root.val)
            return None
        else:
            root.left = self.dfs(root.left, l)
            root.right = self.dfs(root.right, l)
            return root

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result = []
        while root:
            row = []
            root = self.dfs(root, row)
            result.append(row)
        return result

# Method 2


class Solution2:

    def dfs(self, root, heights):
        if root is None:
            return 0
        left_height = self.dfs(root.left, heights)
        right_height = self.dfs(root.right, heights)
        height = max(left_height, right_height) + 1
        heights[height].append(root.val)
        return height

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        heights = defaultdict(list)
        self.dfs(root, heights)
        return heights.values()
