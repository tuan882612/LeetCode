class Solution:
    def canConstruct(self, rn: str, m: str) -> bool:
                
        for i in rn:
            if i in m:
                m = m.replace(i,"",1)
            else: return False
        
        return True