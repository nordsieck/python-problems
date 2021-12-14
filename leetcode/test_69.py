import unittest
from typing import *

class Solution:
    def mySqrt(self, x: int) -> int:
        MAX = 46341 # sqrt(2^31) + 1
        MIN = 0

        high, low = MAX, MIN
        guess = int((high - low) / 2) + low
        while True:
            g2 = guess * guess
            if g2 == x:
                return guess
            elif g2 > x:
                high = guess
            else:
                if (guess + 1) * (guess + 1) > x: return guess
                low = guess
            guess = int((high - low) / 2) + low

            print("high: ", high, " low: ", low, " guess: ", guess)
            
        return 0

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[4, 2],
                [8, 2],
                [9, 3],
                [2147395600, 46340],
        ]
        for a, b in data:
            self.assertEqual(s.mySqrt(a), b)
