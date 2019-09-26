# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        s1, s2 = [(root, 0)], []
        result = [[]]
        level = 0
        while s1 or s2:
            if s1:
                while s1:
                    node, x = s1.pop()
                    if node.left:
                        s2.append((node.left, level))
                    if node.right:
                        s2.append((node.right, level))
                    result[level].append(node.val)
            else:
                while s2:
                    node, x = s2.pop()
                    if node.right:
                        s1.append((node.right, level))
                    if node.left:
                        s1.append((node.left, level))
                    result[level].append(node.val)
            result.append([])
            level += 1
        result.pop()
        return result
