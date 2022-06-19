class Solution:
    def greatestLetter(self, s: str) -> str:
        mx = 0
        res = ""
        
        for i in s:
            
            if i.isupper() and i.lower() in s:
                
                if ord(i) > mx:
                    mx = ord(i)
                    res = i
        
        return res