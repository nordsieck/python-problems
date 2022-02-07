import unittest
from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 10000000
        nums.sort()

        for i in range(len(nums)):

            j, k = i + 1, len(nums) - 1
            while k > j:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target: return target

                if abs(target - result) > abs(target - sum): result = sum
                if sum > target: k -= 1
                else: j += 1

        return result

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [
            # [[0, 0, 0], 1, 0],
            # [[0, 0, 0], 0, 0],

            # [[-1, 2, 1, -4], 1, 2],
            # [[0, 0, 0], 1, 0],
            [[1, 1, 1, 0], 100, 3],
        ]

        for a, b, c in data:
            self.assertEqual(s.threeSumClosest(a, b), c)
