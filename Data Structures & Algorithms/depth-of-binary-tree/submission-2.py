# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [(root, 1)]
        seen = set()
        maxdepth = 1
        while stack:
            node, lvl = stack.pop()
            if lvl > maxdepth: maxdepth = lvl
            if node.left and node.left not in seen:
                stack.append((node.left, lvl + 1))
                seen.add(node.left)
            if node.right and node.right not in seen:
                stack.append((node.right, lvl + 1))
                seen.add(node.right)
        return maxdepth