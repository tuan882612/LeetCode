class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, v in enumerate(nums):
            num = target - v
            if num not in table:
                table[v] = i
            else:
                return [table[num], i]

        return []