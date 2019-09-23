# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def check(self, root, min_val, max_val):
        if not root:
            return True
        if not(root.val > min_val and root.val < max_val):
            return False
        left = self.check(root.left, min_val, root.val)
        right = self.check(root.right, root.val, max_val)
        return left and right

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, float("-inf"), float('inf'))
        
