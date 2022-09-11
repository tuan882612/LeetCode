class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash = {}

        for i in nums:
            if i%2 == 0:
                if i not in hash:
                    hash[i] = 0
                hash[i] += 1
                    
        if len(hash) == 0: return -1
        
        ref = max(hash.values())

        return min([k for k, v in hash.items() if v == ref])