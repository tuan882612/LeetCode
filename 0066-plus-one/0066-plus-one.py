class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        
        for i in digits:
            num += str(i)
            
        num = int(num)+1
        
        res = []
        
        for i in str(num):
            res.append(int(i))
            
        return res