from collections import deque
class Solution:
    def largestPalindromic(self, num: str) -> str:
        hash = {}
        for i in num:
            if i not in hash: hash[i] = 0
            hash[i] += 1
        hash = dict(sorted(hash.items()))
        
        odd = []
        res = deque()
        
        for k, v in hash.items():            
            if v%2 != 0:
                # if v > 1: 
                hash[k] -= 1
                odd.append(k)
                
        if len(odd) != 0: 
            res.append(odd[-1])
        
        for k, v in hash.items():
            while hash[k] != 0:
                res.append(k)
                res.appendleft(k)
                hash[k] -= 2
                
        res = "".join(res).strip('0')
        if len(res) == 0: return '0'
        return res