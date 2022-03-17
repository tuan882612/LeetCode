class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            q = target - n
            if q not in hash:
                hash[n] = i
            else:
                return [hash[q], i]