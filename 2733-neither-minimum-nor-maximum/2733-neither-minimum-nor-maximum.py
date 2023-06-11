class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        mx, mn = max(nums), min(nums)
        
        for i in nums:
            if i != mx and i != mn:
                return i
            
        return -1