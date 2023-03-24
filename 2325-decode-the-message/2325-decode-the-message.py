import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ref = {}
        i = 0
        
        for v in key:
            if v != ' ' and v not in ref:
                ref[v] = i
                i += 1
        
        res = ''
        alp = string.ascii_lowercase
        
        for i in message:
            if i == ' ':
                res += ' '
                continue
            
            res += alp[ref[i]]
            
        return res

            