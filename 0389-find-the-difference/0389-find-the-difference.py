from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        first = Counter(s)
        second = Counter(t)
        
        for i in second:
            if i not in first:
                return i
            
            if second[i] > first[i]:
                return i
            
        return ""
        
        