class Solution:
    def romanToInt(self, s: str) -> int:
        result_number = 0 
        prevous_number = 0
        mapping = {'I':1, 
                'V':5, 
                'X':10, 
                'L':50, 
                'C':100, 
                'D':500, 
                'M':1000}
        for symbol in s[::-1]:
            if mapping[symbol] >= prevous_number:
                result_number += mapping[symbol]
            else:
                result_number -= mapping[symbol]
            prevous_number = mapping[symbol]
        return result_number