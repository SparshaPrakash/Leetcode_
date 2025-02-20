class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we only add an open paren if open < n
        # we only cloing paren if cllsing < open
        # if open = closed paren -> we cant sdd closing paren

        stack = []
        res = []

        def backtrack(openN, closedN):
            if closedN == openN == n:
                res.append("".join(stack))
                return


            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res