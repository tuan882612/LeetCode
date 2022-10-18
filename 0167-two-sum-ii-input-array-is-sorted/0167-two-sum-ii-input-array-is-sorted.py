class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        
        while left < right:
            val = nums[left] + nums[right]
            
            if val == target:
                return [left+1, right+1]
            elif val > target:
                right -= 1
            else:
                left += 1
                
        return []