import unittest
from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        while i >= 0:
            digits[i] += 1
            if digits[i] < 10: return digits
            digits[i] = 0
            i -= 1

        digits.insert(0, 1)
        return digits

class TestSolution(unittest.TestCase):
    def test_fn(self):
        s = Solution()
        data = [[[1], [2]],
                [[9], [1, 0]],
                [[1, 2, 3], [1, 2, 4]],
                [[4, 3, 2, 1], [4, 3, 2, 2]],
                [[0], [1]],
        ]

        for a, b in data:
            self.assertEqual(s.plusOne(a), b)
