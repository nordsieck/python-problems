import unittest
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right
             
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        mid = int(len(nums) / 2)
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]),
                        self.sortedArrayToBST(nums[mid + 1:]))

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        r = TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
        self.assertEqual(s.sortedArrayToBST([-10, -3, 0, 5, 9]), r)

        r = TreeNode(3, TreeNode(1))
        self.assertEqual(s.sortedArrayToBST([1, 3]), r)
