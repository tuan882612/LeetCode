class Solution:
    def decodeString(self, s: str) -> str: 
        res = ""
        num = 0
        stack = []
        
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)    
            elif i == "[":
                stack.append(res)
                stack.append(num)
                res=""
                num=0
            elif i == "]":
                n = stack.pop()
                string = stack.pop()
                res = string + n*res
            else:
                res += i

        return res