class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache [(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False # we wont be able to complete string s then

            match = i < len(s) and (s[i] == p[j] or p[j] ==".") # condition for the first char to match
            if (j + 1) < len(p) and p[j + 1] =="*": # then we have two options
                cache[(i,j)] = ((dfs(i, j + 2)) or # here we dont sue the * so skip the current char and the next *           
                               (match and dfs(i + 1, j))) # we can use the j char multiple times hence we keep j as j and only if the previous char is a match, then we can use this *
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1) # for eg, if we have a b at the end of both the strings, and that i considered a match, and there is no * after the b, so we can increamemt both i and j
                return cache[(i, j)]

            return False # if there is no match in the characters

        return dfs(0, 0)

        