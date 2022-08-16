class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        
        for i in s:
            if i not in hash:
                hash[i] = 0
            hash[i] += 1
            
        hash = sorted(hash.items(), key=lambda x:x[1], reverse=True)
        res = ""
        
        for key, val in hash:
            res += str(key*val)
                
        return res