"""
Author: Samuel Jaden García Muñoz
Date: 23/10/2025
Revised: 
Note:-
Was really quite able to visualize this problem and solve it in one-shot without a lot of tinkering. Very proud.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Dimensions of the board.
        ROWS, COLS = len(board), len(board[0])

        # Recursive depth-first search, pproviding the row, the column, and the current length of the path.
        def dfs(row, column, n):
            # If the length of the word has been achieved, we've found a route that spells our word.
            if n == len(word):
                return True

            # If we're out of bounds or the current position is not the next letter in the word, return false.
            if row < 0 or row >= ROWS or column < 0 or column >= COLS or board[row][column] != word[n]:
                return False

            # If the current position has been visited in this route already, return False.
            if (row, column) in visited:
                return False

            # Otherwise, add it to our route.
            visited.add((row, column))

            # See if there's a potential route in any direction.
            res = (dfs(row + 1, column, n + 1) or     # South 
                    dfs(row - 1, column, n + 1) or     # North
                    dfs(row, column + 1, n + 1) or     # East
                    dfs(row, column - 1, n + 1))       # West

            # Remove the current position from visited (so that it may be explored by another branch of the recursion.)
            visited.remove((row, column))

            # Return the outcome of the search.
            return res

        # Iterate through every position in the board, to use it as the starting position of our search.
        for i in range(ROWS * COLS):
            # Set for tracking visited positions.
            visited = set()
            # Calculate the row and column from the iterator.
            row, column = i // COLS, i % COLS
            # If we find a successful route, we can return immediately.
            if dfs(row, column, 0):
                return True
            # Otherwise, we continue...
        
        # If no route was found, we return False.
        return False

"""
Time Complexity: O(m*n*L^4) (Total positions of the board * length of search word ^ 4 for each potential direction)
Space Complexity: O(L)
"""