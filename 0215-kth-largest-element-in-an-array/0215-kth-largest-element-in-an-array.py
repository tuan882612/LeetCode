class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        for i in range(k):
            val = nums[(len(nums)-1)-i]
        return val
