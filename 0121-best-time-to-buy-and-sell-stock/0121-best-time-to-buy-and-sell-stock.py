class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = prices[0]
        res = 0
        
        for right in range(1,len(prices)):
            cur = min(cur, prices[right])
            res = max(res, prices[right]-cur)
                
        return res