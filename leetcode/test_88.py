import unittest
from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m, n, o = m - 1, n - 1, len(nums1) - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[o], m, o = nums1[m], m - 1, o - 1
            else:
                nums1[o], n, o = nums2[n], n - 1, o - 1

        if n == -1: return
        for i in range(n + 1): nums1[i] = nums2[i]

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]],
                [[1], 1, [], 0, [1]],
                [[0], 0, [1], 1, [1]],
        ]

        for num1, m, num2, n, sol in data:
            s.merge(num1, m, num2, n)
            self.assertEqual(num1, sol)
