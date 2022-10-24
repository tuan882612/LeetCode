class Solution:
    def maxLength(self, arr: List[str]) -> int:
        temp = [""]
        res = 0
        
        for word in arr:
            for i in temp:
                w = i+word
                
                if len(w) == len(set(w)):
                    temp.append(w)
                    res = max(res, len(w))
        return res