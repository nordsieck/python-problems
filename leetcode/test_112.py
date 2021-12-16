import unittest
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        if root.val == targetSum and root.left is None and root.right is None: return True
        return self.hasPathSum(root.left, targetSum - root.val) \
            or self.hasPathSum(root.right, targetSum - root.val)

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        r = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(s.hasPathSum(r, 5), False)

        r = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                     TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
        self.assertEqual(s.hasPathSum(r, 22), True)

        r = None
        self.assertEqual(s.hasPathSum(r, 0), False)
