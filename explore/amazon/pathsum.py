# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        q = deque()
        if not root:
            return False
        q.append((root, root.val))
        while q:
            node, csum = q.popleft()
            if not (node.left or node.right):
                if csum == sum:
                    return True
            else:
                if node.left:
                    q.append((node.left, csum+node.left.val))
                if node.right:
                    q.append((node.right, csum+node.right.val))
        return False

# Definition for a binary tree node.


class Solution2:

    def check(self, root, csum, result):
        if not root:
            return False
        csum += root.val
        if not (root.left or root.right):
            if csum == result:
                return True
        else:
            return self.check(root.left, csum, result) or self.check(root.right, csum, result)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.check(root, 0, sum)
