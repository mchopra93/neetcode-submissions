class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, node):

        if self.parent[node]!= node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, a,b):
        
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] +=1 
        return True




class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total_components = n
        uf = UnionFind(n)

        for a, b in edges:
            if uf.union(a,b):
                total_components-=1
        
        return total_components
        