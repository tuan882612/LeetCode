class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1 
        while start <= end :
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[start] :
                if nums[mid] > target and nums[start] <= target :
                    end = mid - 1
                else :
                    start = mid + 1
            elif nums[mid] < nums[start] :
                if nums[mid] < target and nums[start] > target :
                    start = mid + 1
                else :
                    end = mid - 1
            else:
                start += 1
        return False