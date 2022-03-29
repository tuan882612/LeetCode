class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            cur = abs(i)
            if nums[cur] < 0:
                return cur
            nums[cur] = -nums[cur]