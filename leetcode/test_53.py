import unittest
from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, globe = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > curr + nums[i]:
                curr = nums[i]
            else:
                curr = curr + nums[i]

            if curr > globe: globe = curr

        return globe

class TestSolution(unittest.TestCase):
    def test_MSA(self):
        s = Solution()
        data = [[[0], 0],
                [[-100], -100],
                [[-2,1,-3,4,-1,2,1,-5,4], 6],
                [[5, -10, 6], 6],
                [[20, -10, 2, -10, 20], 22],
                [[30, -20, 10], 30],
        ]

        for a, b in data:
            self.assertEqual(s.maxSubArray(a), b)
