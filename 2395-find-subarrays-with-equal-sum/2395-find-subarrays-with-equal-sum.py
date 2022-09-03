class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        return False if len(set(nums[i-1]+nums[i] for i in range(1, len(nums)))) == len(nums)-1 else True