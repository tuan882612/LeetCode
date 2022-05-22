class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        
        for i in words:
                    
            if (stack and sorted(stack[-1]) != sorted(i)) or not stack:
                stack.append(i)
                
        return stack