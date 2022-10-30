class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = 0
        count = 0
        
        for i in nums:
            if i%6 == 0:
                res += i
                count += 1
                
        return count and res//count