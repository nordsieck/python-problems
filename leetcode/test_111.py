import unittest
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        MAX = 100001
        if root is None: return 0

        l, r = self.minDepth(root.left), self.minDepth(root.right)

        if l == 0 and r > 0: return r + 1
        if r == 0 and l > 0: return l + 1
        return (l if l < r else r) + 1

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(s.minDepth(r), 2)

        r = TreeNode(1, TreeNode(2))
        self.assertEqual(s.minDepth(r), 2)
