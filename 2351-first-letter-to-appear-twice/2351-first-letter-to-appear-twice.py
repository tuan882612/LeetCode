class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash = {}
        
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                return i
            
        return ""