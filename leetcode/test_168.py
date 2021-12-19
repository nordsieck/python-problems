import unittest
from typing import *

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = []
        while columnNumber > 0:
            columnNumber -= 1
            chars.append(columnNumber % 26)
            columnNumber = int(columnNumber / 26)

        chars = [chr(c + ord("A")) for c in chars]
        chars.reverse()
        return "".join(chars)

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[1, "A"],
                [26, "Z"],
                [27, "AA"],
                [28, "AB"],
                [701, "ZY"],
                [2147483647, "FXSHRXW"],
        ]

        for a, b in data:
            self.assertEqual(s.convertToTitle(a), b)
