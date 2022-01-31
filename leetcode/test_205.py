import unittest
from typing import *

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sToT, tToS = {}, {}

        if len(s) != len(t): return False

        for i in range(len(s)):
            if s[i] in sToT:
                if sToT[s[i]] != t[i]: return False
            else:
                if t[i] in tToS: return False
                sToT[s[i]] = t[i]
                tToS[t[i]] = s[i]

        return True

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [["", "", True],
                ["a", "", False],
                ["", "a", False],
                ["a", "a", True],
                ["a", "b", True],
                ["ab", "ba", True],
                ["aa", "ab", False],
                ["ab", "aa", False],

                ["egg", "add", True],
                ["foo", "bar", False],
                ["paper", "title", True],
        ]

        for a, b, c in data:
            self.assertEqual(s.isIsomorphic(a, b), c)
