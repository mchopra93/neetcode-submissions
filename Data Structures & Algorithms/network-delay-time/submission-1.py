class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        distance = {i+1:float('inf') for i in range(n)}
        distance[k]=0
        min_heap = [(0,k)]
        adj_list = defaultdict(list)
        for src,dst,time in times:
            adj_list[src].append((time,dst))

        print(distance)
        print(adj_list)

        while min_heap:
            time_to_node ,curr_node = heapq.heappop(min_heap)

            for time_to_dest, dest in adj_list[curr_node]:
                curr_time = distance[dest]
                if curr_time > time_to_dest+time_to_node:
                    new_time = time_to_dest+time_to_node
                    distance[dest] = new_time
                    heapq.heappush(min_heap,(new_time,dest))
        
        min_distance = max(distance.values())

        if min_distance == float('inf'):
            return -1
        else:
            return min_distance
        

            
                



        