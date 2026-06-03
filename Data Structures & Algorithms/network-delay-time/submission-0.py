class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {node+1:float('inf') for node in range(n)}
        distances[k]=0
        min_heap = [(0,k)]

        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        
        while min_heap:
            cur_time, node = heapq.heappop(min_heap)

            if cur_time > distances[node]:
                continue
            
            #explore neighbors
            for neighbor, weight in graph[node]:
                time_to_neigh =  cur_time + weight
                if time_to_neigh < distances[neighbor]:
                    distances[neighbor] = time_to_neigh
                    heapq.heappush(min_heap, (time_to_neigh, neighbor))

        
        all_times = distances.values()

        if float('inf') in all_times:
            return -1
        
        return max(all_times)



                



        