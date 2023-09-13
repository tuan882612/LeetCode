class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = digits[0]

        for d in digits[1:]:
            num = num*10 + d

        return [int(i) for i in list(str(num+1)) ]
