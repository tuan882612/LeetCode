from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ref = Counter(s)
        
        for i in t:
            if i not in ref:
                return False
            else:
                ref[i] -= 1
                if ref[i] < 0:
                    return False
                
        if sum(ref.values()) > 0:
            return False
            
        return True