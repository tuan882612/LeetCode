class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        
        for i, v in enumerate(nums):
            n = target-v
            if n not in ht:
                ht[v] = i
            else:
                return [ht[n], i]
            
        return []