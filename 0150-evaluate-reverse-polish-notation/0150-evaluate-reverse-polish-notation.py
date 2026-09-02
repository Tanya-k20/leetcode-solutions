class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1. INITIALIZE SETUP
        stack = []
        
        # 2. ITERATE & EVALUATE
        for token in tokens:
            # Check if token is a number
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            # Handle operator evaluation
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    # int() truncates toward zero for '/'
                    stack.append(int(a / b))
        
        # 3. RETURN RESULT
        return stack[-1]