import math

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        
        for i in range(len(nums)):
            cur = nums[i]
            
            for j in range(i, len(nums)):
                cur = self.lcm(cur, nums[j])
                
                if k == cur:
                    res += 1

        return res
    
    def lcm(self, a, b):
        return (a*b) // math.gcd(a,b)