class Solution:
    def canConstruct(self, rn: str, m: str) -> bool:
        hash = {}
        
        for i in rn:
            if i not in hash: hash[i] = 0
            hash[i] += 1
            
        for i in m:
            if i in hash and hash[i] > 0:
                hash[i] -= 1
                
        return sum(hash.values()) == 0