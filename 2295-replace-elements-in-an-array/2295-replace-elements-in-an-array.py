class Solution:
    def arrayChange(self, nums: List[int], op: List[List[int]]) -> List[int]:
        hash = {} 
        for i, v in enumerate(nums):
            hash[v] = i
        
        for x, y in op:
            index = hash[x]
            nums[index] = y
            
            del hash[x]
            hash[y] = index
            
        return nums