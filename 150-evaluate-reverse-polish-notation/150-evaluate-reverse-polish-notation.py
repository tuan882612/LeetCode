class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i not in "-+/*":
                stack.append(int(i))
            else:
                right, left = stack.pop(), stack.pop()
                
                match i:
                    case '+':
                        stack.append(left+right)
                    case '-':
                        stack.append(left-right)
                    case '*':
                        stack.append(left*right)
                    case '/':
                        stack.append(int(operator.truediv(left,right))) 
        return stack.pop()