class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        
        for i, key in enumerate(s):
            
            if key not in hash:
                hash[key] = [i]
            else:
                hash[key].append(i)
                
        for i, key in hash.items():
            if len(key) == 1:
                return key[0]
        
        return -1