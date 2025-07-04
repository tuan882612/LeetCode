class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        table = {}
        for i, v in enumerate(nums):
            n = target - v
            if n not in table:
                table[v] = i 
            else:
                return [i, table[n]]