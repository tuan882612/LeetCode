class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            left = sum(nums[i+1:])
            right = sum(nums[:i])
            
            if left == right:
                return i
            
        return -1