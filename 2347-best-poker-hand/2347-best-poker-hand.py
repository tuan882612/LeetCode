class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        
        hash = {}
        
        for i in ranks:
            
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
            
        num = max(hash.values())
        
        if num >= 3:
            return "Three of a Kind"
        elif num == 2:
            return "Pair"
        return "High Card"