class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for i in range(len(s)):
            e = self.helper(s, i, i)
            o = self.helper(s, i, i+1)
            out = max(out, e, o, key = len)
        return out    
            
    def helper(self, string, l, r):
        while l>=0 and r<len(string):
            if string[l] != string[r]:
                break
            l-=1
            r+=1
        return string[l+1:r]