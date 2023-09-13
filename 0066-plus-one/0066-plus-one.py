class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        digits = digits[::-1]
        for i in range(1, len(digits)):
            if digits[i-1] > 9:
                digits[i-1] = 0
                digits[i] += 1

            
        if digits[-1] > 9:
            digits[-1] = 0
            digits.append(1)
        
        return digits[::-1]