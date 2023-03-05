class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx = 0
        for i in 'aeiou':
            mx+=s[:k].count(i)
            
        ans = mx
        n = len(s)
        for i in range(k, n):
            if s[i] in 'aeiou': 
                mx += 1
                
            if s[i-k] in 'aeiou': 
                mx -= 1
                
            ans = max(ans, mx)
            
        return ans