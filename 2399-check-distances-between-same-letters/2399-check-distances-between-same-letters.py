class Solution:
    def checkDistances(self, s: str, dist: List[int]) -> bool:
        ref = {}
        
        for i in range(26):
            ref[chr(97+i)] = dist[i]
            
        hash = {}
        
        for i, v in enumerate(s):
            if v not in hash:
                hash[v] = i+1
            else:
                hash[v] = abs(hash[v]-i)
                
                if ref[v] != hash[v]:
                    return False

        return True