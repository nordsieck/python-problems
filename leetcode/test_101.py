import unittest
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSame(p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False

        outside = Solution.isSame(p.left, q.right)
        inside = Solution.isSame(p.right, q.left)

        return outside and inside and p.val == q.val
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return Solution.isSame(root.left, root.right)
        
class TestSolution(unittest.TestCase):
    def teestFn(self):
        s = Solution()

        r = None
        self.assertEqual(s.isSymmetric(r), True)
        
        r = TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)),
                     TreeNode(2, None, TreeNode(3, None, None)))
        self.assertEqual(s.isSymetric(r), False)

        r = TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
                     TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)))
        self.assertEqual(s.isSymetric(r), True)

        r = TreeNode(1, TreeNode(2, TreeNode(2, None, None), None),
                     TreeNode(2, TreeNode(2, None, None), None))
        self.assertEqual(s.isSymetric(r), False)
