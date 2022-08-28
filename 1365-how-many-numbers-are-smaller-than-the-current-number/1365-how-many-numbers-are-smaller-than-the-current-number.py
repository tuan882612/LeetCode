class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ref = sorted(nums)
        res = []
        
        for i in nums:
            n = 0
            
            while ref[n] < i: n += 1
            res.append(n)
        return res