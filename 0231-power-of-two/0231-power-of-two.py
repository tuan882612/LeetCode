class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        for i in range(31):
            if n == 2**i:
                return True
            
        return False