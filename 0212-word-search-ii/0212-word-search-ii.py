class TrieNode:
    def __init__(self):
        self.children = {} # can use a list as well
        self.endOfWord = False

    def addNode(self, word):
        cur = self # root node

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur= cur.children[c]
        cur.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addNode(w)

        rows, cols= len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):    # r, c- coordinates on the board, node- current character in Trie, word- word we have formed so far
            if r < 0 or c < 0 or r == rows or c ==cols or board[r][c] not in node.children or (r, c) in visited:
               return
            visited.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)


            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)

        