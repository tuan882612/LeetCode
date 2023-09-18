class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0

        neg = 0
        for i in nums:
            neg += i < 0

        return 1 if neg%2 == 0 else -1