class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # None means not end of word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # First store all of the words in a TrieTree
        # Then iterate through each of the chars 
        # If the root has a children with the current ith char then go dfs
        # Once we find the word, we append the current used cords into a hashset for O1 lookup
        # Then we can skip everytime we find it in the has set for the backtracking 

        root = TrieNode()
        cur = root

        for word in words:
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word
            cur = root 

        
        res = []
        height = len(board)
        width = len(board[0])

        def dfs(row, col, visited, tree):
            if row >= height or col >= width or row < 0 or col < 0:
                return
            if (row, col) in visited:
                return
            
            visited.add((row,col))
            current_char = board[row][col]

            if current_char in tree.children:
                tree = tree.children[current_char]
                if tree.word:
                    res.append(tree.word)
                    tree.word = None
                dfs(row + 1, col, visited, tree)
                dfs(row - 1, col, visited, tree)
                dfs(row, col + 1, visited, tree)
                dfs(row, col - 1, visited, tree)
            
            
            visited.remove((row,col))

        for r in range(height):
            for c in range(width):
                dfs(r,c, set(), root)
        return res
                

            


        
