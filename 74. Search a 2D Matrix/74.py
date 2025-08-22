"""
Author: Samuel Jaden García Muñoz
Date: 22/08/2025
Note:-

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Boundaries of the matrix
        ROWS, COLUMNS = len(matrix), len(matrix[0])

        # Left and right pointers for binary search.
        left, right = 0, ROWS * COLUMNS - 1

        # Normal structure of a binary search.
        while left <= right:
            # Calculate the middle index.
            middle = (left + right) // 2

            # Calculate the row and the column.
            row = middle // COLUMNS # Whole division by columns
            column = middle % COLUMNS # Modulus by columns

            if matrix[row][column] == target:
                return True

            elif matrix[row][column] > target:
                right = middle - 1

            else:
                left = middle + 1

        return False
    
"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""