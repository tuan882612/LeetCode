class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = temp = nums[0]
        for x in nums[1:]:
            temp = max(x, temp + x)
            res = max(res, temp)
        return res