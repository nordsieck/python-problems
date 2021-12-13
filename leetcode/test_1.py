import unittest
from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            if target - v in seen: return sorted([i, seen[target - v]])
            seen[v] = i

class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        s = Solution()
        data = [[[1, 2], 3, [0, 1]],
                [[2, 7, 11, 15], 9, [0, 1]],
                [[3, 2, 4], 6, [1, 2]],
                [[3, 3], 6, [0, 1]],
        ]

        for a, b, c in data:
            self.assertEqual(s.twoSum(a, b), c, str([a, b, c]))
