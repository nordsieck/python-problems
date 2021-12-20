import unittest
from typing import *

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        parts = []
        parts.append(s[:spaces[0]])

        for i in range(len(spaces) - 1):
            parts.append(s[spaces[i]: spaces[i + 1]])

        parts.append(s[spaces[-1]:])

        return " ".join(parts)

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [["LeetcodeHelpsMeLearn", [8, 13, 15], "Leetcode Helps Me Learn"],
                ["icodeinpython", [1, 5, 7, 9], "i code in py thon"],
                ["spacing", [0, 1, 2, 3, 4, 5, 6], " s p a c i n g"],
        ]

        for a, b, c in data:
            self.assertEqual(s.addSpaces(a, b), c)
