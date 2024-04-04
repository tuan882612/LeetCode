class Solution:
    def arraySign(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] == 0:
                return 0

            nums[0] *= nums[i]

        if nums[0] == 0:
            return 0

        return 1 if nums[0] > 0 else -1