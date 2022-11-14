class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        for i in range(31):
            temp = 2**i
            if n == temp:
                return True
            
        return False