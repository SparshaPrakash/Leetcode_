class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == "..":
                # go back one step
                if stack:
                    stack.pop()
            elif not part or part == '.':
                # do nothing
                continue
            else:
                # add to stack this is a path or directory name
                stack.append(part)
        final_str = '/' + '/'.join(stack)
        return final_str
        