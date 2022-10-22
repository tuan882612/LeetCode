class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        temp = []
        
        for i in nums:
            temp.append(i)
            
            if len(temp) > 1:
                res += min(temp)
                temp = []

        return res