from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ht1, ht2 = Counter(s), Counter(t)
        
        for k, v in ht1.items():
            if v != ht2[k]:
                return False
            
        return True