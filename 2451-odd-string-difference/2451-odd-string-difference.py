class Solution:
    def oddString(self, words: List[str]) -> str:
        res = []
        
        for word in words:
            calc = [ord(word[i])-ord(word[i-1]) for i in range(1, len(word))]
            res.append((word,calc))
            
        res = sorted(res, key=lambda x:x[1])
        
        if res[0][1] != res[1][1]: return res[0][0]
        if res[-1][1] != res[0][1]: return res[-1][0]
        
        for i in range(1, len(res)):
            print(res[i])
            if res[i][1] != res[i-1][1]:
                return res[i][0]