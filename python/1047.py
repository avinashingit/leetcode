class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack:
                if ch == stack[-1]:
                    stack.pop()
                    continue
            stack.append(ch)
        return ''.join(stack)
