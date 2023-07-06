class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = ptr2 = 0
        n1, n2 = len(word1), len(word2)
        res = ''
        
        for _ in range(max(n1, n2)):
            if ptr1 < n1:
                res += word1[ptr1]
                ptr1 += 1
            
            if ptr2 < n2:
                res += word2[ptr2]
                ptr2 += 1

        return res