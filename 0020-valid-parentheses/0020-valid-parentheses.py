class Solution(object):
    def isValid(self, s):
        stack = []
        stackList = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in stackList:
                if stack and stack[-1] == stackList[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False