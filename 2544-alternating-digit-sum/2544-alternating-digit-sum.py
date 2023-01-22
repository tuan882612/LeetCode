class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res, sign = 0, 1
        
        for i in str(n):
            res += sign * int(i)
            sign = -sign
            
        return res
        