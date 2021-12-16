import unittest
from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1

        while i < j:
            if not s[i : i + 1].isalnum():
                i += 1
                continue
            if not s[j : j + 1].isalnum():
                j -= 1
                continue
            if s[i] != s[j]: return False
            i, j = i + 1, j - 1

        return True

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [["a", True],
                ["ab", False],
                ["A man, a plan, a canal: Panama", True],
                ["race a car", False],
                [" ", True],
        ]

        for a, b in data:
            self.assertEqual(s.isPalindrome(a), b, a)
