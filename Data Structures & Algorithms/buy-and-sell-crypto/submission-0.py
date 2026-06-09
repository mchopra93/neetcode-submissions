class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while left<len(prices)-1:

            diff = prices[right]-prices[left]
            print(f"left:{left} right:{right} profit={diff}, {prices[right]} - {prices[left]}")

            if diff > max_profit:
                print(f"max profit={diff}, {prices[right]} - {prices[left]}")
                max_profit = diff
            else:
                right+=1
            if right ==len(prices):
                left+=1
                right=left+1
            
        return max_profit
            

