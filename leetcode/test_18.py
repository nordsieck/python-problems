import unittest
from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for a in range(len(nums)):
            if a != 0 and nums[a] == nums[a - 1]: continue

            for b in range(a + 1, len(nums)):
                if b != a + 1 and nums[b] == nums[b - 1]: continue

                c, d = b + 1, len(nums) - 1
                while d > c:
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])

                        c += 1
                        while nums[c] == nums[c - 1] and d > c: c += 1

                        d -= 1
                        while nums[d] == nums[d + 1] and d > c: d -= 1

                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    else:
                        c += 1
        return result
        

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [
            [[0, 0, 0, 0], 0, [[0, 0, 0, 0]]],
            [[], 0, []],
            [[1, 2, 3, 4, 5], 12, [[1, 2, 4, 5]]],
            
            [[1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]],
            [[2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]],
        ]

        for a, b, c in data:
            self.assertEqual(s.fourSum(a, b), c)
