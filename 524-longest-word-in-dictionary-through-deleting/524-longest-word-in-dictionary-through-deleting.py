class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        arr = sorted(dictionary, key = lambda x:(-len(x),x))
        
        for word in arr:
            count = 0
            
            for char in s:
                if count < len(word) and word[count] == char:
                    count += 1
                    
            if count == len(word):
                return word
        return ""