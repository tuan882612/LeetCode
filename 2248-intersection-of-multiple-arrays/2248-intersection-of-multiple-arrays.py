class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hash = {}
        
        for row in nums:
            for i in set(row):
                if i not in hash:
                    hash[i] = 0
                hash[i] += 1
            
        return sorted([k for k, v in hash.items() if v == len(nums)])