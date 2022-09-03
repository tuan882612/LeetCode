class Solution:
    def arrayChange(self, nums: List[int], op: List[List[int]]) -> List[int]:
        hash = {}
        
        for x, y in reversed(op):
            hash[x] = hash.get(y, y)

        for i, v in enumerate(nums):
            if v in hash:
                nums[i] = hash[v]
                
        return nums