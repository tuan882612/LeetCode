class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if not tokens:
            return 0
        operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
        }
        stack = []

        for token in tokens:
            if token in operators:
                stack.append(operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack[0]