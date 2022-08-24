class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: return False
        if n == 1: return True
        num = 1
        
        for i in range(len(str(n))*2):
            num *= 3
            if num == n: return True
        return False