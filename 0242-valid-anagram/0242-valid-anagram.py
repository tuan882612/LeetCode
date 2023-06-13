from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ref = set(s)
        
        for i in ref:
            if s.count(i) != t.count(i):
                return False
            
        return True