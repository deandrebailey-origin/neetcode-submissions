class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 0:
            return False

        for p in s:
            if p == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif p == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif p == ")":
                if not stack or stack.pop() != "(":
                    return False
            else:
                stack.append(p)

        print(stack)
        if len(stack) > 0:
            return False
        return True
