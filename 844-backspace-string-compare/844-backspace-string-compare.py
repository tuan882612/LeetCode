class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def func(string):
            stack = []
            
            for i in string:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
                    
            return "".join(stack)
        
        return func(s) == func(t)