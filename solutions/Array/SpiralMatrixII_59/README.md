# Intuition

The problem is asking to generate a square matrix filled with elements from 1 to n^2 in spiral order. The spiral starts from the top left corner and moves inwards in a clockwise direction.

## Approach

Initialize a n x n matrix with all elements as 0.
Define four variables top, bottom, left, right to denote the current boundary of the matrix we are working on.
Start filling the matrix, the order of filling is top row -> right column -> bottom row -> left column.
After filling the top row, increment top pointer.
After filling the right column, decrement right pointer.
After filling the bottom row, decrement bottom pointer.
After filling the left column, increment left pointer.
Continue this process until top <= bottom and left <= right.

## Complexity

- Time complexity: O(n^2), because we have to fill n^2 elements into the matrix.
- Space complexity: O(n^2), for storing the output matrix.

## Code

```py
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> s.generateMatrix(3)
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        """
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix        
```
