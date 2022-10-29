class Solution:
    def oddString(self, words: List[str]) -> str:
        res = {}
        
        for word in words:
            tup = tuple(ord(word[i])-ord(word[i-1]) for i in range(1, len(word)))
            
            if tup not in res:
                res[tup] = [word]
            else:
                res[tup].append(word)
                
        for arr, word in res.items():
            if len(word) == 1:
                 return word[0]