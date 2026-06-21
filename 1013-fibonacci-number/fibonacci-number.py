class Solution:
    def fib(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        
        prev2 = 0  # F(n-2)
        prev1 = 1  # F(n-1)
        
        
        for i in range(2, n + 1):
            current = prev1 + prev2
           
            prev2 = prev1
            prev1 = current
            
        return prev1