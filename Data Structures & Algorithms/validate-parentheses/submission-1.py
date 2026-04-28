class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:

            if x == '(' or x == '{' or x == '[':
                stack.append(x)
                continue
            if len(stack)>0 and x  in [')',']','}']:
                if (stack[-1]== '(' and x == ')') or (stack[-1]== '[' and x == ']') or (stack[-1]== '{' and x == '}'):
                    stack.pop()
                    continue
                else:
                    return False
            else:
                return False

        if len(stack)>0:
            return False    
        
        return True