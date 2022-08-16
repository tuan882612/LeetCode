class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        
        for i, key in enumerate(s):
            if key not in hash:
                hash[key] = i
            else:
                hash[key] = -1
                
        for i in hash.values():
            if i != -1:
                return i
            
        return -1