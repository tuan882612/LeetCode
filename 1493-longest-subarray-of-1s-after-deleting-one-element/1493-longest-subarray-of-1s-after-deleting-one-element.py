class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = l = piv = 0
        
        for r, n in enumerate(nums):
            piv += n
            
            while piv < r-l:
                piv -= nums[l]
                l += 1
                
            res = max(res, r-l)
            
        return res