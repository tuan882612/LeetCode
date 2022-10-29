class Solution:
    def oddString(self, words: List[str]) -> str:
        res = {}
        
        for word in words:
            arr = tuple(ord(word[i])-ord(word[i-1]) for i in range(1, len(word)))
            
            if arr not in res:
                res[arr] = [word]
            else:
                res[arr].append(word)
                
        for arr, word in res.items():
            if len(word) == 1:
                 return word[0]