class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []
        for ch in s:
            if ch == "]":
                exp = ""
                while stack[-1] != '[':
                    exp = stack.pop() + exp
                stack.pop()
                count = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    count = stack.pop() + count
                count = int(count)
                for _ in range(count):
                    result += exp
                stack.append(result)
                result = ""
            else:
                stack.append(ch)
        return "".join(stack)
