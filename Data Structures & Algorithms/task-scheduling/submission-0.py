from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)

        max_heap = [(-cnt,task) for task,cnt in counts.items()]

        heapq.heapify(max_heap)

        time = 0

        cooldown_queue = deque()
        actual_schedule = []

        while max_heap or cooldown_queue:
            time+=1

            if max_heap:
                cnt,task = heapq.heappop(max_heap)
                actual_schedule.append(task)

                new_cnt = cnt + 1

                if new_cnt!=0:
                    cooldown_queue.append((new_cnt, task, time+n))
            else:
                # No tasks available -> CPU is idle
                actual_schedule.append("idle")
            
            if cooldown_queue and cooldown_queue[0][2] == time:
                ready_cnt, ready_task, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap,(ready_cnt,ready_task))
        print(actual_schedule)
        return time




        