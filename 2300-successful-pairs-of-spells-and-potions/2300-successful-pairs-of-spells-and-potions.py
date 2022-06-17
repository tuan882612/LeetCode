class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        
        for i in spells:
            left, right = 0,len(potions)
            find = success/i
            
            while left < right:
                mid = left+(right-left)//2
                
                if potions[mid] >= find:
                    right = mid
                    
                else:
                    left = mid + 1
                    
            res.append(len(potions)-left)
            
        return res