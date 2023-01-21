class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        pre = post = 0
        
        for i in nums:
            pre += i
            
            while i > 0:
                post += i%10
                i = i//10

        return pre-post