class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        temp = ""
        res = 0

        while "01" in s:
            temp = s.replace("01","10")
            s = temp
            res += 1
            
        return res