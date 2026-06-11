# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def dfs(node):

            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            curr_dia = left_height+right_height

            self.max_d = max(curr_dia, self.max_d)

            return 1 + max(left_height, right_height)

        dfs(root)
        return self.max_d
        