class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        
        for i in s:
            if i not in hash:
                hash[i] = 0
            hash[i] += 1
            
        hash = dict(reversed(sorted(hash.items(), key = lambda x:x[1])))
        res = ""
        
        for i in hash:
            while hash[i] != 0:
                res += i
                hash[i] -= 1
                
        return res