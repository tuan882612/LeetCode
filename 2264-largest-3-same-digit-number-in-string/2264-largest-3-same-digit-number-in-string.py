class Solution:
    def largestGoodInteger(self, num: str) -> str:
        hash = {}
        res = set()
        
        for i in range(3,len(num)+1):
            temp = num[i-3:i]
            
            for j in temp:
                if j not in hash:
                    hash[j] = 1
                else:
                    hash[j] += 1
            
            if len(hash) == 1:
                if temp == None:
                    res.add('000')
                else:
                    res.add(temp)
                    
            hash = {}
        
        if len(res) >= 1:
            return max(res)
        return ""