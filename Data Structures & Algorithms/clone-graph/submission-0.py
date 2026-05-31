"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}
        if not node:
            return None

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]

            copy = Node(node.val)
            visited[node] = copy
            for neighbor in node.neighbors:
                    cloned_neighbor = dfs(neighbor)
                    copy.neighbors.append(cloned_neighbor)
            return copy
        return dfs(node)



        