class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        
        for i in words:
            
            if not stack:
                stack.append(i)
                    
            elif stack and sorted(stack[-1]) != sorted(i):
                stack.append(i)
                
        return stack