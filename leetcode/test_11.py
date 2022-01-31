import unittest
from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        updateArea = lambda: min(height[low], height[high]) * (high - low)
        area = updateArea()

        while high > low:
            if height[low] > height[high]:
                h = high
                while h > low and height[high] >= height[h]: h -= 1
                high = h
            else:
                l = low
                while high > l and height[low] >= height[l]: l += 1
                low = l
            _area = updateArea()
            if _area > area: area = _area

        return area
        

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [
            [[0, 0], 0],
            [[1, 0], 0],
            [[0, 1], 0],
            [[1, 1], 1],
            [[0, 1, 0, 1, 0], 2],

            [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
            [[1, 1], 1],
        ]

        for a, b in data:
            self.assertEqual(s.maxArea(a), b)
