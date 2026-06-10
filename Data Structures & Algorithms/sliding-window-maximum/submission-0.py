class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_heap = [(-nums[i],i) for i in range(k)]
        heapq.heapify(max_heap)

        result = [-max_heap[0][0]]
        
        for r in range(k,len(nums)):
            heapq.heappush(max_heap,(-nums[r], r))
            
            while max_heap[0][1] <= r-k:
                heapq.heappop(max_heap)
            
            result.append(-max_heap[0][0])
        
        return result
            
        