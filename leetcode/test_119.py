import unittest
from typing import *

class Solution:
    def fact(a, b = 1):
        if a == 0: return 1
        prod = 1
        for i in range(b + 1, a + 1):
            prod *= i
        return prod
    
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex + 1):
            a, b = i, rowIndex - i
            if a < b: a, b = b, a
            result.append(int(Solution.fact(rowIndex, a) / Solution.fact(b)))
        return result
            

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[0, [1]],
                [1, [1, 1]],
                [2, [1, 2, 1]],
                [3, [1, 3, 3, 1]],
                [4, [1, 4, 6, 4, 1]],
                [5, [1, 5, 10, 10, 5, 1]],
                [6, [1, 6, 15, 20, 15, 6, 1]],
        ]

        for a, b in data:
            self.assertEqual(s.getRow(a), b)

    def testFact(self):
        data = [[4, 1, 24],
                [4, 2, 12],
                [4, 3, 4],
                [4, 4, 1],
                [0, 1, 1],
        ]
        for a, b, c in data:
            self.assertEqual(Solution.fact(a, b), c)
