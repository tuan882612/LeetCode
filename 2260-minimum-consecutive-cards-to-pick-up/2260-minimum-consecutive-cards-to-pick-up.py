class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hash = {}
        res = float('inf')
        
        for index, num in enumerate(cards):
            
            if num not in hash:
                hash[num] = index
            else:
                res = min(index - hash[num]+1, res)
                hash[num] = index
        
        if res == float('inf'):
            return -1
        return res
            
            