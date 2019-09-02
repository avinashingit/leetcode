class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    ch = stack[-1]
                    if c == '}' and ch != '{':
                        return False
                    elif c == ']' and ch != '[':
                        return False
                    elif c == ')' and ch != '(':
                        return False
                    else:
                        stack.pop()
        return len(stack) == 0
