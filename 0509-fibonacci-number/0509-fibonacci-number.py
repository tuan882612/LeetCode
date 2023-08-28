class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        h = [0, 1]
        
        for i in range(2, n):
            h[i%2] = h[0] + h[1]

        return h[0] + h[1]