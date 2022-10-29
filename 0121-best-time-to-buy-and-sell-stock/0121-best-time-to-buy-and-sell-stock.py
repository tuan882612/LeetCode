class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        cur = prices[0]
        res = 0
        
        for right in range(1,len(prices)):
            if cur > prices[right]:
                cur = prices[right]
                
            res = max(res, prices[right]-cur)
                
        return res