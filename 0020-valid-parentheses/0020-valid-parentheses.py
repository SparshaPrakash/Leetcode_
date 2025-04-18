class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in pairs:  # means its a closing parenthesis
                if stack and stack[-1]  == pairs[c]:    # stack shousnt be emtpty
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False
        


