class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            q = target - n
            if n not in hash:
                hash[q] = i
            else:
                return [hash[n], i]