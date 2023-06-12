class Solution:
    def smallestString(self, s: str) -> str:
        i = 0
        n = len(s)
        s = list(s)
        
        while i < n and s[i] == 'a':
            i += 1
            
        if i == n:
            s[-1] = 'z'
            
        while i < n and s[i] != 'a':
            s[i] = chr(ord(s[i]) - 1)
            i += 1
            
        return ''.join(s)