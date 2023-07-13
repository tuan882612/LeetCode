from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ht = Counter(s)
        res = 0
        one = False
        
        for k, v in ht.items():
            if v%2 == 0:
                res += v
            else:
                res += v-1
                one = True
            
        return res+1 if one else res
                
                