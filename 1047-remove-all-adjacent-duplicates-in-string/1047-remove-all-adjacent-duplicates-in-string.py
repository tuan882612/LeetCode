class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = [s[0]]
        
        for i in s[1:]:
            if res and res[-1] == i:
                res.pop()
            else:
                res.append(i)

        return "".join(res)