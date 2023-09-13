class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums
        
        l = 0
        for r in range(n):
            if nums[r] != 0:
                if nums[l] == 0:
                    nums[r], nums[l] = nums[l], nums[r]

                if nums[l] != 0:
                    l += 1