# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = deque()
        
        #Initialize the Queue with Root
        queue.append(root)
        result = []

        while queue:
            # size of queue -> number of elements at that level
            level_size = len(queue)

            last_node = None
            
            while level_size:
                last_node = queue.popleft()
                if last_node.left:
                    queue.append(last_node.left)
                if last_node.right:
                    queue.append(last_node.right)
                level_size-=1
            result.append(last_node.val)
        
        return result
            

            


        