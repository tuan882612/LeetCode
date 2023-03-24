class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        res = 0
        
        for i in range(left, right + 1):
            if self.validate(words[i]):
                res += 1
            
        return res
    
    def validate(self, word: str) -> bool:
        vowel = 'aeiou'
        return word[0] in vowel and word[-1] in vowel
            