class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        
        for i in range(1,len(searchWord)+1):
            temp = []
            
            for prod in products:
                if prod[:i] == searchWord[:i]: 
                    temp.append(prod)
                    
                if len(temp)==3:
                    break
            res.append(temp)
            
        return res