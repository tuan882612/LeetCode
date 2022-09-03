class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        hash = set()
        
        for i in range(1, len(nums)):
            sm = nums[i-1]+nums[i]
            
            if sm in hash: return True
            hash.add(sm)
        
        return False