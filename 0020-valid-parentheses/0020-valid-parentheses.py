class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {")":"(", "}":"{", "]":"["}

        for val in s:
            if val in d:
                if stack and stack[-1] == d[val]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(val)

        return True if not stack else False

        














