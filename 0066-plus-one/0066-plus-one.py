class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        for i in range(len(digits)-2, -1, -1):
            if digits[i+1] == 10:
                digits[i+1] = 0
                digits[i] += 1
                
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits

        return digits