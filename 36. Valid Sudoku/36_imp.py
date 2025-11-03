"""
Author: Samuel Jaden García Muñoz
Date: 03/11/2025
Revised: 
Note:-
Reduced amount of passes.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Default dicts for storing each row/col/square without having to worry about missing keys.
        rowSets = collections.defaultdict(set)
        colSets = collections.defaultdict(set)
        squareSets = collections.defaultdict(set)

        # Iterate through every row...
        for i in range(len(board)):
            # Iterate through every column...
            for j in range(len(board[0])):
                # If the current position is empty, continue
                if board[i][j] == ".":
                    continue
                # Otherwise, check if this position is a duplicate in either the current row,
                # column, or square.
                if (board[i][j] in rowSets[i] or 
                    board[i][j] in colSets[j] or
                    board[i][j] in squareSets[(i//3, j//3)]):
                    # If an invalid (repeat) number is found, then we know that this is not a valid sudoku.
                    return False

                # If no duplicate was found, add the items to the corresponding set.
                rowSets[i].add(board[i][j])
                colSets[j].add(board[i][j])
                squareSets[(i//3, j//3)].add(board[i][j])

        # If no duplicate have been found, the sudoku is valid.
        return True

"""
Time Complexity: O(9*9) => O(1)
Space Complexity: O(9*9*3) => O(1)
"""