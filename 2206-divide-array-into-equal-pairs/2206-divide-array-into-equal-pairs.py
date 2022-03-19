class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0: return False
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in hash.values():
            if i % 2 != 0:
                return False
        return True