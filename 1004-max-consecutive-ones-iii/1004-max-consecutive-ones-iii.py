class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = l = 0
        
        for r, n in enumerate(nums):
            k -= n == 0
            
            if k < 0:
                k += nums[l] == 0
                l += 1
                
            res = max(res, r-l+1)
            
        return res