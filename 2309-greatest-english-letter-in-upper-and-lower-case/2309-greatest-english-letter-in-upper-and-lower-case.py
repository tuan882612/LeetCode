class Solution:
    def greatestLetter(self, s: str) -> str:
        hash = {}
        
        for i in s:
            
            if i.isupper() and i.lower() in s:
                
                if i.upper() not in hash:
                    hash[i.upper()] = 1

                else:
                    hash[i.upper()] += 1
        
        if len(hash) > 0:
            return max(hash)
        
        return ""