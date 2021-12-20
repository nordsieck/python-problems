import unittest
from typing import *

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        periods, curr = [], 1

        for i in range(1, len(prices)):

            if prices[i] == prices[i - 1] - 1:
                curr += 1
            else:
                periods.append(curr)
                curr = 1

        periods.append(curr)
        periods = [int(n * (n + 1) / 2) for n in periods]

        sum = 0
        for i in range(len(periods)): sum += periods[i]

        return sum

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[[3, 2, 1, 4], 7],
                [[8, 6, 7, 7], 4],
                [[1], 1],
        ]

        for a, b in data:
            self.assertEqual(s.getDescentPeriods(a), b)
