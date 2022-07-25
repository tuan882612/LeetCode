class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        arr = sorted(dictionary, key = lambda x:(-len(x),x))
        
        for word in arr:
            it = iter(s)
                    
            if all(x in it and x for x in word):
                return word
        return ""