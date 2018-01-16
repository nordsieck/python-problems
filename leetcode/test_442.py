import unittest

class Solution:
    def findDuplicates(self, nums):
        dup = []

        for n in nums:
            val = abs(n)
            if nums[val - 1] < 0:
                dup.append(val)
            else:
                nums[val - 1] *= -1

        return dup

class TestSolutions(unittest.TestCase):
    def test_findDuplicates(self):
        self.assertEqual(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])

if __name__ == '__main__':
    unittest.main()
