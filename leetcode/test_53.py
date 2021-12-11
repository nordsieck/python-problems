import unittest
from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MAX_INT = 10001 # max value used is 10^4
        MIN_INT = -10001 # min value used is -10^4
        
        sum = 0
        sums = [(sum := sum + nums[i]) for i in range(len(nums))]

        maxSum, max, min = sums[0], MIN_INT, 0
        for i in range(len(sums)):
            if sums[i] < min:
                min = sums[i]
                max = MIN_INT
            elif sums[i] > max:
                max = sums[i]
                if max - min > maxSum:
                    maxSum = max - min
                
        return maxSum

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
