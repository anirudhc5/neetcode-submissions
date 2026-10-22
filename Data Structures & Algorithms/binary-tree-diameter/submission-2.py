# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_height(root):
            if not root: return 0
            return 1 + max(max_height(root.left), max_height(root.right))
        if not root: return 0
        leftmax = 0 if not root.left else max_height(root.left)
        rightmax = 0 if not root.right else max_height(root.right)
        s = leftmax + rightmax
        return max(max(self.diameterOfBinaryTree(root.left),
        self.diameterOfBinaryTree(root.right)),s)