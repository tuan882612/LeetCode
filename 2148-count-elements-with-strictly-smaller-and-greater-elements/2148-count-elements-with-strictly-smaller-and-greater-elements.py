class Solution:
    def countElements(self, nums: List[int]) -> int:
        res = 0
        
        for i in nums:
            
            if min(nums)<i<max(nums):
                res += 1
                
        return res
                