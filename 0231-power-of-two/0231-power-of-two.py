class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (1 << 31) % n == 0