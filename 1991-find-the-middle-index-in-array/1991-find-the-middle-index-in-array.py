class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # left, right = nums[0], sum(nums[:len(nums)-1])
        # left, right = 0, sum(nums)
        
        for i, n in enumerate(nums):
            left = sum(nums[i+1:])
            right = sum(nums[:i])
            
            if left == right:
                return i
            
        return -1