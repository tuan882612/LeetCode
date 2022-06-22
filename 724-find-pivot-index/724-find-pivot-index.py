class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        
        for i, val in enumerate(nums):
            left += val
            
            if left == right:
                return i
            
            right -= val
            
        return -1