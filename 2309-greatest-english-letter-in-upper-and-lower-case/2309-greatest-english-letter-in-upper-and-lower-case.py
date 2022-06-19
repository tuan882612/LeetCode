class Solution:
    def greatestLetter(self, s: str) -> str:
        map = [0]*26 
        for i in s:
            if i.isupper():# check for uppercase
                map[ord(i)-ord('A')] |= 1 
            else:# for lowercase
                map[ord(i) - ord('a')] |= 2 
        for i in range(25,-1,-1):
            if map[i] == 3:
                return chr(i+ord("A"))# return greatest letter
        return ''# return empty string if not found