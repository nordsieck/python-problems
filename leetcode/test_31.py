import unittest
from typing import *

# todo: right now this solution is nlogn. We can optimzie this solution more because the numbers after cut are reverse sorted. We just have to handle the two swapped values
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1: return nums
        
        cut = len(nums) - 2
        while nums[cut] >= nums[cut + 1] and cut >= 0: cut -= 1

        if cut == -1:
            nums.sort()
            return nums

        swapPos = cut + 1
        for i in range(cut + 2, len(nums)):
            if nums[i] > nums[cut] and nums[swapPos] > nums[i]: swapPos = i

        nums[swapPos], nums[cut] = nums[cut], nums[swapPos]
        nums[cut + 1:] = sorted(nums[cut + 1:])
        return nums

        

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[[1], [1]],
                [[1, 1], [1, 1]],

                [[1, 2], [2, 1]],
                [[2, 1], [1, 2]],

                [[1, 2, 3], [1, 3, 2]],
                [[1, 3, 2], [2, 1, 3]],
                [[2, 1, 3], [2, 3, 1]],
                [[2, 3, 1], [3, 1, 2]],
                [[3, 1, 2], [3, 2, 1]],
                [[3, 2, 1], [1, 2, 3]],
                
                [[1, 1, 5], [1, 5, 1]],
                [[1, 5, 1], [5, 1, 1]],
                [[5, 1, 1], [1, 1, 5]],
        ]

        for a, b in data:
            self.assertEqual(s.nextPermutation(a), b)


# [1, 2, 3] -> [1, 3, 2] -> [2, 1, 3] -> [2, 3, 1] -> [3, 1, 2] -> [3, 2, 1]
