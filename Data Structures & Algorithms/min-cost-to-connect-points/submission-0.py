class UnionFind:
    def __init__(self, size):
        # Initially every node is its own parent
        self.parent = list(range(size))
        self.rank = [1]*size
    
    def find(self, i):

        if self.parent[i]==i:
            return i
        
        self.parent[i]=self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] +=1
        return True



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        pipes = []
        
        # Step 1: Meticulously build every possible pipeline connection
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                pipes.append((dist, i, j))
        
        # Step 2: Sort pipelines by distance (cheapest/shortest first)
        pipes.sort()
        
        # Step 3: Run Kruskal's loop using Union-Find
        uf = UnionFind(n)
        min_cost = 0
        pipes_laid = 0
        
        for dist, u, v in pipes:
            if uf.union(u, v):
                min_cost += dist
                pipes_laid += 1
                
                # Optimization: An MST always finishes when we reach exactly N - 1 connections
                if pipes_laid == n - 1:
                    break
                    
        return min_cost


        