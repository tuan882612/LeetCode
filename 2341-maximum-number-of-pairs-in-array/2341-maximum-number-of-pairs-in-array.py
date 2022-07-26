class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        count = 0
		
        for n in nums_set:
            if nums.count(n) % 2 == 1:
                count += 1
                
        return [(len(nums)-count)//2, count]
