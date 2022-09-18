class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        
        left = 0
        res = 0
        n = len(s)
        
        for right in range(1,n):
            if ord(s[right])-ord(s[right-1])!=1:
                left = right     
                
            res = max(res, right-left+1)
            
        return res