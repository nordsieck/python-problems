import unittest
from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1, 1]]

        while len(result) < numRows:
            row, i, j = [1], 0, 1
            while j < len(result[-1]):
                row.append(result[-1][i] + result[-1][j])
                i, j = i + 1, j + 1
            row.append(1)
            result.append(row)

        return result[:numRows]
            

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[1, [[1]]],
                [3, [[1], [1, 1], [1, 2, 1]]],
                [5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]],
                
        ]

        for a, b in data:
            self.assertEqual(s.generate(a), b)
