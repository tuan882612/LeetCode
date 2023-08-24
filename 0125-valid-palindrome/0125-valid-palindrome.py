class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i.lower() for i in s if i.isalnum())
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]: return False
            left, right = left+1, right-1

        return True