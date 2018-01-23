import unittest

class Solution:
    def isToeplitzMatrix(self, matrix):
        
        for rStart in range(len(matrix) - 1):
            r, c = rStart, 0
            val = matrix[r][c]
            while r < len(matrix) and c < len(matrix[0]):
                if matrix[r][c] != val: return False
                r, c = r+1, c+1

        for cStart in range(1, len(matrix[0]) - 1):
            r, c = 0, cStart
            val = matrix[r][c]
            while r < len(matrix) and c < len(matrix[0]):
                if matrix[r][c] != val: return False
                r, c = r+1, c+1

        return True

class TestSolution(unittest.TestCase):
    def test_isToeplitzMatrix(self):
        self.assertEqual(Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)
        self.assertEqual(Solution().isToeplitzMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), False)
        self.assertEqual(Solution().isToeplitzMatrix([[0, 0, 0], [0, 0, 0], [0, 1, 0]]), False)
        self.assertEqual(Solution().isToeplitzMatrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]]), False)
