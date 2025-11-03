"""
Author: Samuel Jaden García Muñoz
Date: 03/11/2025
Revised: 
Note:-

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Iterate through every row...
        for i in range(len(board)):
            # Create a set for tracking occurrences of values.
            visited = set()
            # Iterate through every column...
            for j in range(len(board[i])):
                # If an empty value is found, continue.
                if board[i][j] == ".":
                    continue
                # If a duplicate value is found, return False.
                if board[i][j] in visited:
                    return False
                # Otherwise, add it to the visited set.
                visited.add(board[i][j])

        # Same as above, checking for all values in a given column.
        for i in range(len(board)):
            visited = set()
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in visited:
                    return False
                visited.add(board[j][i])

        # Similar as above...
        for i in range(len(board)):
            visited = set()
            # Iterate through every row in the square...
            for j in range(3):
                # Iterate through every column in the square...
                for k in range(3):
                    # Calculate the row and column by using division to get to the square's position.
                    row = i // 3 * 3 + j
                    col = i % 3 * 3 + k

                    # Same as before...
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in visited:
                        return False
                    visited.add(board[row][col])
        
        # If no duplicates have been found, return True.
        return True

"""
Time Complexity: O(9*9*3) => O(1)
Space Complexity: O(9) => O(1)
"""