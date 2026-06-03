class Solution:
    def climbStairs(self, n: int) -> int:

        number_of_distinct = 0
        if n==0:
            return 0
        
        mem = {}
        
        def climb(rem_steps):
            
            if rem_steps<0:
                return 0
            
            if rem_steps==0:
                return 1
            
            if rem_steps in mem:
                return mem[rem_steps]

            mem[rem_steps] = climb(rem_steps-1) + climb(rem_steps-2)

            return mem[rem_steps]
    
        return climb(n)


        