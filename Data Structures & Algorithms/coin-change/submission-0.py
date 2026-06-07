from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # The memory bank: stores (current_choice, rem_amount) -> fewest_coins
        memo = {}

        def CoinChoice(current_choice: int, coins: List[int], rem_amount: int) -> int:
            # 1. Check if we already calculated this exact scenario
            if (current_choice, rem_amount) in memo:
                return memo[(current_choice, rem_amount)]

            # 2. Base Cases
            if rem_amount == 0:
                return 0
            if rem_amount < 0 or current_choice == len(coins):
                return -1

            results = []

            # Choice 1: Take the current coin (stay on the same index to allow reuse)
            choice1 = CoinChoice(current_choice, coins, rem_amount - coins[current_choice])
            if choice1 >= 0:
                results.append(1 + choice1)

            # Choice 2: Skip the current coin completely (move to the next index)
            choice2 = CoinChoice(current_choice + 1, coins, rem_amount)
            if choice2 >= 0:
                results.append(choice2)

            # 3. Choose the absolute minimum or return -1 if both paths failed
            if not results:
                final_ans = -1
            else:
                final_ans = min(results)

            # 4. Save the answer in memory before returning
            memo[(current_choice, rem_amount)] = final_ans
            return final_ans

        # Fix: Properly pass the index, the coins list, and the starting target amount
        return CoinChoice(0, coins, amount)

            



            
            
        

        