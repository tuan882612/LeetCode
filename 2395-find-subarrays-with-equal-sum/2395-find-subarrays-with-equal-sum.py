class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        hash = set()
        
        for i in range(1, len(nums)):
            hash.add(nums[i-1]+nums[i])
        
        return False if len(hash) == len(nums)-1 else True