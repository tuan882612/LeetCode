class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        hash = {}
        
        for i in letters:
            
            if i > target:
                if i not in hash:
                    hash[ord(i)] = i
        if len(hash) == 0:
            return min(letters)
        return hash[min(hash.keys())]