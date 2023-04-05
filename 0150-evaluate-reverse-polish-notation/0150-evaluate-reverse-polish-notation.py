class Solution:
    def opr_table(self, op: str, n1: int, n2: int) -> int:
        match op:
            case '+': return n1+n2
            case '-': return n1-n2
            case '*': return n1*n2
            case '/': return n1/n2
            
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for i in tokens:
            if i in '+-*/':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(int(self.opr_table(i, n1, n2)))
            else:
                stack.append(int(i))

        return stack[0]   
