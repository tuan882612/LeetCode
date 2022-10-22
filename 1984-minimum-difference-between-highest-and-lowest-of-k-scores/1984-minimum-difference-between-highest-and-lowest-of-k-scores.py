class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        nums = sorted(nums)
        res = nums[k-1] - nums[0]

        for i in range(k, len(nums)):
            res = min(res, nums[i] - nums[i-k + 1])
            print(nums[i] - nums[i - k + 1])
        return res
