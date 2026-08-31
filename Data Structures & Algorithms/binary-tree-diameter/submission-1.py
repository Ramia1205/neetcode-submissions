# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            # Empty node has height 0
            if not node:
                return 0

            # Height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Longest path passing through this node
            diameter = max(diameter, left_height + right_height)

            # Return this node's height to its parent
            return 1 + max(left_height, right_height)

        dfs(root)
        return diameter