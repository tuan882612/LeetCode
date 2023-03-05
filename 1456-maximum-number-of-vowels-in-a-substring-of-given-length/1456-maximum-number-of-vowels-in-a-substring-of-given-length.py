class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        count = 0
        
        for i in s[:k]:
            if i in vowels:
                count += 1
                
        res = count
        for end in range(k, len(s)):
            start = end - k + 1
            
            if s[start-1] in vowels:
                count -= 1
                
            if s[end] in vowels:
                count += 1
                
            res = max(res, count)

        return res 