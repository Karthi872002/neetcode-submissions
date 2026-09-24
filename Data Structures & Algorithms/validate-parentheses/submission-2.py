class Solution:
    def isValid(self, s: str) -> bool:

        bracket_pairs = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        stack = []
        for bracket in s:
            if  bracket in bracket_pairs:
                if not stack:
                    return False
                if stack[-1] == bracket_pairs.get(bracket):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        if len(stack) > 0:
            return False
        
        return True