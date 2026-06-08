# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        queue = deque()
        if root:
            queue.append(root)
        
        result = []

        while queue:
            level_elements = []
            breadth = len(queue)
            for _ in range(breadth):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level_elements.append(curr.val)
            result.append(level_elements)
        return result


        