class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Initialize All Cost to Infinity
        cost_to_dest = {i:(float('inf'),i) for i in range(n)}
        # start node
        cost_to_dest[src] = (0,src)

        for _ in range(k+1):
            snapshot = dict(cost_to_dest)
            for s,d,p in flights:
                curr_cost,curr_hop = snapshot[s]
                new_cost,new_hop = cost_to_dest[d]
                if curr_cost != float('inf') and curr_cost + p < new_cost:
                    cost_to_dest[d] = (curr_cost+p, s)
        
        final_cost = cost_to_dest[dst][0]
        return final_cost if final_cost!=float('inf') else -1






        