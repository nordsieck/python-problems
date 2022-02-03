import unittest
from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        i = 0
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]: continue
            
            j, k = i + 1, len(nums) - 1
            while k > j:

                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

                    j += 1
                    while nums[j] == nums[j - 1] and k > j: j += 1

                    k -= 1
                    while nums[k] == nums[k + 1] and k > j: k -= 1

                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return results
                
                
            
        

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[[0, 0, 0], [[0, 0, 0]]],
                
                [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
                [[], []],
                [[0], []],
        ]

        for a, b in data:
            self.assertEqual(s.threeSum(a), b)
