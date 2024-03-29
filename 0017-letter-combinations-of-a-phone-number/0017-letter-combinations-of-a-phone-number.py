class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        graph = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z']
        }

        visited = []
        stack = []

        def dfs(i):
            if i == len(digits):
                visited.append("".join(stack))
            else:
                print(visited, stack)
                for l in graph[digits[i]]:
                    stack.append(l)
                    dfs(i+1)
                    stack.pop()

        dfs(0)
        return visited
        