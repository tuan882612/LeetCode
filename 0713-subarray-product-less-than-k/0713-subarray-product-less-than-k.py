class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, n, res = 0, 1, 0

        for r in range(len(nums)):
            n *= nums[r]            

            while n >= k and l <= r:                    
                n /= nums[l]
                l += 1

            res += r - l + 1                

        return res