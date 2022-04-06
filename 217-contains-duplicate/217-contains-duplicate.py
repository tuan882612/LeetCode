class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for i in nums:
            if i in hash:
                return True
            hash.add(i)
        return False