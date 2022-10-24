class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        
        for i in nums:
            if i not in hash:
                hash.add(i)
            else:
                return True
            
        return False