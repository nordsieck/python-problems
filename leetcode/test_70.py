import unittest
from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        num, prev = 1, 1
        for i in range(n - 1): num, prev = num + prev, num
        return num

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[2, 2],
                [1, 1],
                [3, 3],
        ]

        for a, b in data:
            self.assertEqual(s.climbStairs(a), b)
