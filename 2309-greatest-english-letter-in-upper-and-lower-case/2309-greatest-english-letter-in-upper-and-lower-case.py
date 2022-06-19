class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ""
        
        for i in s:
            
            if i.isupper() and i.lower() in s:
                
                if i > res:
                    res = i
        
        return res